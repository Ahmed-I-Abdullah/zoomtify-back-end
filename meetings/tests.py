from django.test import TestCase
from meetings.models import User, Meeting, Contact
import datetime


class TestCreateContact(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='test', password='12345678910')

        Contact.objects.create(
            first_name='test',
            last_name='contact',
            phone_number='+16135550141',  # fake phone number from https://fakenumber.org/canada
            associated_user=test_user
        )

    def test_contact_content(self):
        contact = Contact.objects.get(id=1)
        first_name = f'{contact.first_name}'
        last_name = f'{contact.last_name}'
        phone_number = f'{contact.phone_number}'
        associated_user = contact.associated_user
        self.assertEqual(first_name, 'test')
        self.assertEqual(last_name, 'contact')
        self.assertEqual(phone_number, '+16135550141')
        self.assertEqual(associated_user, User.objects.get(id=1))

    def test_str(self):
        contact = Contact.objects.get(id=1)
        self.assertEqual(str(contact), 'Contact: test, +16135550141')


class TestCreateMeeting(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='test', password='12345678910')

        test_contact = Contact.objects.create(
            first_name='test',
            last_name='contact',
            phone_number='+16135550141',  # fake phone number from https://fakenumber.org/canada
            associated_user=test_user
        )

        date_time_obj = datetime.datetime(2021, 11, 28, 23, 55, 59, 342380)

        test_meeting = Meeting.objects.create(
            user=test_user,
            name='refinement meeting',
            link='http://example.com/bike',
            start_date_time=date_time_obj,
        )
        test_meeting.notified_contacts.add(test_contact)

    def test_meeting_content(self):
        meeting = Meeting.objects.get(id=1)
        user = meeting.user
        name = f'{meeting.name}'
        link = f'{meeting.link}'
        start_date_time = f'{meeting.start_date_time}'
        notified_contact = meeting.notified_contacts.all()[0]
        self.assertEqual(notified_contact, Contact.objects.get(id=1))
        self.assertEqual(user, User.objects.get(id=1))
        self.assertEqual(name, 'refinement meeting')
        self.assertEqual(link, 'http://example.com/bike')
        self.assertEqual(start_date_time, '2021-11-28 23:55:59.342380+00:00')

    def test_str(self):
        meeting = Meeting.objects.get(id=1)
        self.assertEqual(
            str(meeting), 'Meeting: refinement meeting, 2021-11-28 23:55:59.342380+00:00')
