from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ProtectedArea, Location
from .serializers import ProtectedAreaSerializer, LocationSerializer
from django.db import connection
from django.shortcuts import render
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
            serializer.save()
            return JsonResponse(serializer.data, status=201)        
        return JsonResponse(serializer.errors, status=400)
    
@csrf_exempt  
def update_location_province(request):
    if request.method == 'POST':
        try:
            location = Location.objects.get(sub_loc=request.POST['sub_loc'])
            if(location is not None):        
                location.province = request.POST['province']
                location.save()
                return HttpResponse('Location updated for sub_loc: '+request.POST['sub_loc'])
            return HttpResponse('Location does not exist or input data is invalid')  
        except Exception as e:
            return HttpResponse('Input data is invalid or sub_loc does not exist')  
    if request.method == 'GET':
        return render(request, 'update_location.html') 
    
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
            return HttpResponse(json.dumps(serializer.data, indent=4), content_type="application/json")