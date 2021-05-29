from rest_framework import generics
from meetings.models import Meeting, Contact
from .serializers import MeetingSerializer, ContactSerializer

class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer   


