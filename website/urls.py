from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_home, name='homepage'),
]