import json
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from phoneaddressbook.models import PhoneInfo
from phoneaddressbook.serializers import PhoneInfoSerializer
from django.contrib.auth.models import User


class PhoneInfoTests(APITestCase):
    
    def setUp(self):
        test_user = User.objects.create(username='henry', password='dkdkdkdkdk')
        PhoneInfo.objects.create(first_name='john', last_name='smith', relationship='friend', mobile_number='01919191', landline_number='03030303', owner=test_user)
        PhoneInfo.objects.create(first_name='jane', last_name='jones', relationship='fwb', mobile_number='02223232', landline_number='0443334', owner=test_user)
    
    def test_send_get_request_to_phonenumbers_check_status_code(self):
        '''
        Send a get request to localhost:8000/phonenumbers to ensure we get correct status code back
        '''
        response = self.client.get('/phonenumbers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    
    def test_send_get_request_to_phonenumbers_check_json(self):
        '''
        Send a get request to localhost:8000/phonenumbers to ensure we get correct status code back
        '''
        response = self.client.get('/phonenumbers/')
        phone_info = PhoneInfo.objects.all()
        serializer = PhoneInfoSerializer(phone_info, many=True, context={'request': response})
        self.assertEqual(response.data, serializer.data)
        
