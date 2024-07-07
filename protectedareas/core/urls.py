from django.urls import path
from . import api

urlpatterns = [
    path('locations/', api.location_list, name='locationlist'), #get all locations
    path('protected-areas/', api.protected_area_list, name='protectedareaslist'), #get all protected areas
    path('location-protected-areas/<str:sub_loc>/', api.location_protected_areas_list, name='locationprotectedareaslist'), #get all protected areas in a location
    path('national-parks/', api.national_parks_list, name='nationalparkslist') #get all national parks


    
]