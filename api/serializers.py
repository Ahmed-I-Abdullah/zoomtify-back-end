from django.db.models import fields
from rest_framework import serializers
from meetings.models import Meeting, Contact

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'name', 'link', 'start_date_time', 'message', 'notified_contacts')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact      
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'associated_user')