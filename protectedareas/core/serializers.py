from rest_framework import serializers
from .models import ProtectedArea,Location

# Serializers define the API representation.
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ProtectedAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectedArea
        fields = '__all__'
    
    def get_province(self, obj):
        return obj.location.sub_loc if obj.location else None

class NationalParksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProtectedArea
        fields = '__all__'