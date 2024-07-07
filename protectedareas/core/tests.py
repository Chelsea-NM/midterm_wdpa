from django.test import TestCase

# Create your tests here. 
def test_post(self):
    print('test_post')
    data = {
      sub_loc: 'ZA-LE',
      province: 'Lesotho'
    }
    response = self.client.post(reverse('locations'), data, content_type='application/x-www-form-urlencoded')
    assertEqual(response, 'ZA-LE') 