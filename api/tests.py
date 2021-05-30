from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from meetings.models import Contact

class ContactsTest(APITestCase):
    def test_view_contacts(self):
        end_point = reverse('api:contact_listcreate')
        response = self.client.get(end_point, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_contacts(self):
        end_point = reverse('api:contact_listcreate')
        contact = {
            'first_name': 'test', 
            'last_name': 'contact', 
            'phone_number': '+16135550141'
            }    
        response = self.client.post(end_point, contact, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)    

class MeetingsTest(APITestCase):
    def test_view_meetings(self):
        end_point = reverse('api:meeting_listcreate')
        response = self.client.get(end_point, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_meetings(self):
        end_point = reverse('api:meeting_listcreate')
        test_contact = Contact.objects.create(
            first_name = 'test', 
            last_name = 'contact', 
            phone_number = '+16135550141' # fake phone number from https://fakenumber.org/canada
            )
        meeting = {
            'name': 'daily standup',
            'link': 'https://example.com/brake/boundary.html',
            'start_date_time': '2021-05-21T04:57:00Z',
            'message': 'Hi, I have a meeting in a few minutes',
            'notified_contacts': [
                1
            ]
         }  
        response = self.client.post(end_point, meeting, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)            
