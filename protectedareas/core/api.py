from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import ProtectedArea, Location
from .serializers import ProtectedAreaSerializer, LocationSerializer
from django.db import connection

import json
from django.http import HttpResponse

@csrf_exempt
def location_list(request):
    if request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return HttpResponse(json.dumps(serializer.data, indent=4), content_type="application/json")
    
    elif request.method == 'POST':
        serializer = LocationSerializer(data=request.POST)
        if serializer.is_valid():
            #print('serializer.is_valid()')
            serializer.save()
            return JsonResponse(serializer.data, status=201)        
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt  
def update_location_province(request, sub_loc,province_name):
    if request.method == 'POST':
        location = Location.objects.get(sub_loc=sub_loc)
        if(location is not None):        
            location.province = province_name
            location.save()
            return HttpResponse('Location update for sub_loc: '+sub_loc)
        return HttpResponse('Location does not exist')
    
@csrf_exempt
def protected_area_list(request):
    if request.method == 'GET':
        protected_areas = ProtectedArea.objects.all()
        serializer = ProtectedAreaSerializer(protected_areas, many=True)
        return HttpResponse(json.dumps(serializer.data, indent=4), content_type="application/json")

@csrf_exempt  
def location_protected_areas_list(request, sub_loc):
    if request.method == 'GET':
        protected_areas = ProtectedArea.objects.filter(sub_loc=sub_loc)
        serializer = ProtectedAreaSerializer(protected_areas, many=True)
        return HttpResponse(json.dumps(serializer.data, indent=4), content_type="application/json")
        
@csrf_exempt
def national_parks_list(request):
    if request.method == 'GET':
        protected_areas = ProtectedArea.objects.filter(desig_eng__contains='National Park').select_related('sub_loc').order_by('-rep_area')
        serializer = ProtectedAreaSerializer(protected_areas, many=True)
        return HttpResponse(json.dumps(serializer.data, indent=4), content_type="application/json")

@csrf_exempt
def test_function(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM core_protectedarea")
            row = cursor.fetchone()
            count_value = row[0]
            #total_protected_areas = ProtectedArea.objects.raw("SELECT COUNT(*) FROM core_protectedarea")
            return HttpResponse(json.dumps(serializer.data, indent=4), content_type="application/json")