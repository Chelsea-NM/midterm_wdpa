from django.test import TestCase
from django.models import ProtectedArea,Location
from rest_framework import serializers

# Create your tests here. 
#location cant be equal to sub_loc
class ProtectedAreaTestCase(TestCase):
  """
  Test case for the ProtectedArea model.
  """

  def setUp(self):
    self.location = Location.objects.create(sub_loc='Bulacan')
    self.protected_area = ProtectedArea.objects.create(name='Bulacan Protected Area', location=self.location)
    
  def test_protected_area(self):
    self.assertEqual(self.protected_area.location.sub_loc, 'Bulacan')
    
  def test_protected_area_fail(self):
    self.assertNotEqual(self.protected_area.location.sub_loc, 'Pampanga')

#test serializers
class ProtectedAreaSerializerTestCase(TestCase):
  """
  Test case for the ProtectedAreaSerializer class.
  """

  def setUp(self):
    self.location = Location.objects.create(sub_loc='Bulacan')
    self.protected_area = ProtectedArea.objects.create(name='Bulacan Protected Area',location=self.location)
    self.serializer = ProtectedAreaSerializer(instance=self.protected_area)
    
  def test_contains_expected_fields(self):
    data = self.serializer.data
    self.assertEqual(set(data.keys()), set(['id', 'name', 'location']))
    
  def test_location(self):
    data = self.serializer.data
    self.assertEqual(data['location'], self.location.sub_loc)
    
  def test_location_fail(self):
    data = self.serializer.data
    self.assertNotEqual(data['location'], 'Pampanga')
    
  def test_protected_area(self):
    data = self.serializer.data
    self.assertEqual(data['name'], self.protected_area.name)
    
  def test_protected_area_fail(self):
    data = self.serializer.data
    self.assertNotEqual(data['name'], 'Pampanga Protected Area')
