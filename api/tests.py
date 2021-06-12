from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from meetings.models import Contact
from django.contrib.auth.models import User


class ContactsTest(APITestCase):
    def test_view_contacts(self):
        end_point = reverse('api:contact_listcreate')
        test_user = User.objects.create_user(
            username='test', password='12345678910')

        self.client.login(username=test_user.username,
                          password='12345678910')
        response = self.client.get(end_point, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_contacts(self):
        end_point = reverse('api:contact_listcreate')
        test_user = User.objects.create_user(
            username='test', password='12345678910')

        self.client.login(username=test_user.username,
                          password='12345678910')
        contact = {
            'first_name': 'test',
            'last_name': 'contact',
            'phone_number': '+16135550141',
            'associated_user': 1
        }

        response = self.client.post(end_point, contact, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class MeetingsTest(APITestCase):
    def test_view_meetings(self):
        end_point = reverse('api:meeting_listcreate')

        test_user = User.objects.create_user(
            username='test', password='12345678910')

        self.client.login(username=test_user.username,
                          password='12345678910')
        response = self.client.get(end_point, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_meetings(self):
        end_point = reverse('api:meeting_listcreate')
        test_user = User.objects.create_user(
            username='test', password='12345678910')

        self.client.login(username=test_user.username,
                          password='12345678910')
        Contact.objects.create(
            first_name='test',
            last_name='contact',
            phone_number='+16135550141',  # fake phone number from https://fakenumber.org/canada
            associated_user=test_user
        )

        meeting = {
            'user': 1,
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
