

#import model
from .models import Garden

#import utils
import datetime
from django.shortcuts import redirect


def update(request):
    print(request.method)
    if(request.method == "GET"):
	
        fertilizer = request.GET.get("fertilizer", None)
        weed = request.GET.get("weed", None)
        water = request.GET.get("water", None)
        rain = request.GET.get("rain", None)
        print(request.GET)
        
        garden = Garden.objects.all()[0]
        if(fertilizer):
            garden.fertilizer_time = datetime.datetime.now()
            garden.fertilizer_user = request.user
        
        if(weed):
            garden.weed_time = datetime.datetime.now()
            garden.weed_user = request.user
            
        if(water):
            garden.water_time = datetime.datetime.now()
            garden.water_user = None
        garden.save()
            
    return redirect('/garden')