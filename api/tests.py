from django.http import response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from meetings.models import Contact, Meeting
from django.contrib.auth.models import User
from rest_framework.test import APIClient
import datetime


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


class ContactsPermissionsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_user_one = User.objects.create_user(
            username='test1', password='12345678910')
        User.objects.create_user(
            username='test2', password='12345678910')

        Contact.objects.create(
            first_name='test',
            last_name='contact',
            phone_number='+16135550141',  # fake phone number from https://fakenumber.org/canada
            associated_user=test_user_one
        )

    def test_valid_user(self):
        client = APIClient()

        test_user_one_username = User.objects.get(id=1).username

        client.login(username=test_user_one_username,
                     password='12345678910')

        end_point = reverse(('api:contact_detail'), kwargs={'pk': 1})

        response = client.put(
            end_point, {
                'first_name': 'test',
                'last_name': 'contact',
                'phone_number': '+16135550141',
                'associated_user': 1
            }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_user(self):
        client = APIClient()

        test_user_two_username = User.objects.get(id=2).username

        client.login(username=test_user_two_username,
                     password='12345678910')

        end_point = reverse(('api:contact_detail'), kwargs={'pk': 1})

        response = client.put(
            end_point, {
                'first_name': 'test',
                'last_name': 'contact',
                'phone_number': '+16135550141',
                'associated_user': 1
            }, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


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


class MeetingsPermissionsTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        test_user_one = User.objects.create_user(
            username='test1', password='12345678910')
        User.objects.create_user(
            username='test2', password='12345678910')

        test_contact = Contact.objects.create(
            first_name='test',
            last_name='contact',
            phone_number='+16135550141',  # fake phone number from https://fakenumber.org/canada
            associated_user=test_user_one
        )

        date_time_obj = datetime.datetime(2021, 11, 28, 23, 55, 59, 342380)

        test_meeting = Meeting.objects.create(
            user=test_user_one,
            name='refinement meeting',
            link='http://example.com/bike',
            start_date_time=date_time_obj,
            message="test message",
        )
        test_meeting.notified_contacts.add(test_contact)

    def test_valid_user(self):
        client = APIClient()

        test_user_one_username = User.objects.get(id=1).username

        client.login(username=test_user_one_username,
                     password='12345678910')

        end_point = reverse(('api:meeting_detail'), kwargs={'pk': 1})

        response = client.put(
            end_point, {
                'user': 1,
                'name': 'daily standup',
                'link': 'https://example.com/brake/boundary.html',
                'start_date_time': '2021-05-21T04:57:00Z',
                'message': 'Hi, I have a meeting in a few minutes',
                'notified_contacts': [
                    1
                ]
            }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_user(self):
        client = APIClient()

        test_user_two_username = User.objects.get(id=2).username

        client.login(username=test_user_two_username,
                     password='12345678910')

        end_point = reverse(('api:meeting_detail'), kwargs={'pk': 1})

        response = client.put(
            end_point, {
                'user': 1,
                'name': 'daily standup',
                'link': 'https://example.com/brake/boundary.html',
                'start_date_time': '2021-05-21T04:57:00Z',
                'message': 'Hi, I have a meeting in a few minutes',
                'notified_contacts': [
                    1
                ]
            }, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
