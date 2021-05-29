from django.db.models import fields
from rest_framework import serializers
from meetings.models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('id', 'name', 'link', 'start_date_time', 'message', 'notified_contacts')