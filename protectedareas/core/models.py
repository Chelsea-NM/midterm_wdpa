from django.db import models

class Location(models.Model):
    sub_loc = models.CharField(max_length=255, primary_key=True)
    province = models.CharField(max_length=255)

class ProtectedArea(models.Model):
    wdpaid = models.IntegerField(primary_key=True)
    wdpa_pid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    desig_eng = models.CharField(max_length=255)
    desig_type = models.CharField(max_length=255)
    marine = models.CharField(max_length=10)
    rep_m_area = models.FloatField(blank=True, null=True)
    gis_m_area = models.FloatField(blank=True, null=True)
    rep_area = models.FloatField(blank=True, null=True)
    gis_area = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=255)
    status_yr = models.IntegerField()
    gov_type = models.CharField(max_length=255)
    own_type = models.CharField(max_length=255)
    mang_auth = models.CharField(max_length=255)
    sub_loc = models.ForeignKey(Location, blank=True, null=True, on_delete=models.CASCADE)
    parent_iso3 = models.CharField(max_length=3)
