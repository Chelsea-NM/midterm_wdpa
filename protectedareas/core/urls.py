from django.urls import path
from . import api
from . import views 

urlpatterns = [
    path('', views.index, name='index') ,
    path('import-protectedareas', views.import_wdoecm_data, name='import-wdpaoecm-data'),
    path('import-locations', views.import_location_data, name='import-location-data'),
    
    path('locations/', api.location_list, name='locationlist'), #get all locations
    path('protected-areas/', api.protected_area_list, name='protectedareaslist'), #get all protected areas
    path('location-protected-areas/<str:sub_loc>/', api.location_protected_areas_list, name='locationprotectedareaslist'), #get all protected areas in a location
    path('location/update/<str:sub_loc>/<str:province_name>', api.update_location_province, name='updatelocationprovince'),
    path('national-parks/', api.national_parks_list, name='nationalparkslist'),#get all national parks

    path('location/update/', api.update_location_province, name='updatelocation'),
   

    
]