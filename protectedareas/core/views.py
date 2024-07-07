from django.shortcuts import render
from .models import ProtectedArea, Location
import csv

def import_wdoecm_data(request):
    file_path = 'protectedareas\core\csv-data\WDOECM_data.csv' 
    c = 0
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Create or get the Location instance
            location, created = Location.objects.get_or_create(
            sub_loc=row['SUB_LOC']
            )
            
            ProtectedArea.objects.create(
                wdpaid=row['WDPAID'],
                wdpa_pid=row['WDPA_PID'],
                name=row['NAME'],  
                desig_eng=row['DESIG_ENG'],
                desig_type=row['DESIG_TYPE'],
                marine=row['MARINE'],        
                rep_m_area=row['REP_M_AREA'],
                gis_m_area=row['GIS_M_AREA'],
                rep_area=row['REP_AREA'],
                gis_area=row['GIS_AREA'],        
                status=row['STATUS'], 
                status_yr=row['STATUS_YR'],
                gov_type=row['GOV_TYPE'],
                own_type=row['OWN_TYPE'],
                mang_auth=row['MANG_AUTH'],
                sub_loc=location,
                parent_iso3=row['PARENT_ISO3'],
            )
            c += 1
    print('function::import_data')
    return render(request, 'import_csv_data.html', {'insert_count': c, 'file_path': file_path})

def import_location_data(request):
    file_path = 'protectedareas\core\csv-data\LOCATION_data.csv' 
    c = 0
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
            Location.objects.create(
                sub_loc=row['SUB_LOC'],
                province=row['PROVINCE']
            )
            c += 1
    return render(request, 'import_csv_data.html', {'insert_count': c, 'file_path': file_path})
