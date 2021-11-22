from django.urls import path
from . import views



urlpatterns = [    
    ###Auth Related#####
    path('post', views.ParkingLogs.Post, name='ParkingLogs_Port')
]