from rest_framework import generics
from meetings.models import Meeting
from .serializers import MeetingSerializer

class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer


