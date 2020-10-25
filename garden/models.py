from django.db import models
from django.contrib.auth.models import User

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


#import datetime
import datetime


class Garden(models.Model):
    water_time = models.DateTimeField(auto_now_add=True)
    water_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="water")
    
    fertilizer_time = models.DateTimeField(auto_now_add=True)
    fertilizer_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="fertilizer")
    
    weed_time = models.DateTimeField(auto_now_add=True)
    weed_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="weed")
    
    def time_to_water(self):
        return self.water_time + datetime.timedelta(days=14)
    
    def time_to_fertilizer(self):
        return self.fertilizer_time + datetime.timedelta(days=14)
        
    def time_to_weed(self):
        return self.weed_time + datetime.timedelta(days=14)
        
    
    

class GardenPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
    
    def get_context(self, request):
        context = super().get_context(request)

        # Add extra variables and return the updated context
        garden = Garden.objects.all()[0]
        context['water_start_time'] = garden.water_time
        context['water_end_time'] = garden.time_to_water()
        context['water_user'] = "rain"
        if(garden.water_user):
            context['water_user'] = garden.water_user.get_full_name()
        
        context['fertilizer_start_time'] = garden.fertilizer_time
        context['fertilizer_end_time'] = garden.time_to_fertilizer()
        context['fertilizer_user'] = garden.fertilizer_user.get_full_name()
        
        context['weed_start_time'] = garden.weed_time
        context['weed_end_time'] = garden.time_to_weed()
        context['weed_user'] = garden.weed_user.get_full_name()
        
        
        return context
    
