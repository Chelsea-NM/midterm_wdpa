from django.db import models

class Location(models.Model):
    """
    Represents a location with sub-location and province information.
    """

    sub_loc = models.CharField(max_length=255, primary_key=True)
    province = models.CharField(max_length=255)

class ProtectedArea(models.Model):
    """
    Represents a protected area.

    Attributes:
        wdpaid (int): The unique identifier for the protected area.
        wdpa_pid (str): The PID (Protected Area ID) of the protected area.
        name (str): The name of the protected area.
        desig_eng (str): The English designation of the protected area.
        desig_type (str): The type of designation for the protected area.
        marine (str): Indicates whether the protected area is marine or not.
        rep_m_area (float): The reported marine area of the protected area.
        gis_m_area (float): The GIS (Geographic Information System) marine area of the protected area.
        rep_area (float): The reported area of the protected area.
        gis_area (float): The GIS area of the protected area.
        status (str): The status of the protected area.
        status_yr (int): The year of the status of the protected area.
        gov_type (str): The type of government responsible for the protected area.
        own_type (str): The type of ownership for the protected area.
        mang_auth (str): The managing authority of the protected area.
        sub_loc (Location): The sub-location of the protected area (foreign key).
        parent_iso3 (str): The ISO3 code of the parent location.
    """
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
