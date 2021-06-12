from rest_framework import generics
from meetings.models import Meeting, Contact
from .serializers import MeetingSerializer, ContactSerializer
from whatsappNotifier.scheduler import schedule_message
from rest_framework.permissions import BasePermission
import threading

class MeetingPermission(BasePermission):
    message = "you are not authorized to edit this meeting."
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class ContactPermission(BasePermission):
    message = "you are not authorized to edit this contact."
    def has_object_permission(self, request, view, obj):
        return obj.associated_user == request.user        

class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

    def get_queryset(self, *args, **kwargs):
     return Meeting.objects.all().filter(user=self.request.user)

    def post(self, request, *args,**kwargs):
        def my_shcedule(name):
            print("thread starting: ", name)
            meeting_date_time = request.POST.get('start_date_time')
            notified_contacts= request.POST.getlist('notified_contacts')
            receivers_phone_numbers = [str(Contact.objects.get(id=int(contact)).phone_number) for contact in notified_contacts]
            for phone_number in receivers_phone_numbers:
                schedule_message(phone_number, meeting_date_time)

        scheduling_thread = threading.Thread(target=my_shcedule, args=(1,))
        scheduling_thread.start()        
        
        return self.create(request, *args, **kwargs)

class MeetingItem(generics.RetrieveUpdateDestroyAPIView, MeetingPermission):
    permission_classes=[MeetingPermission]
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer        

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer   

    def get_queryset(self, *args, **kwargs):
     return Contact.objects.all().filter(associated_user=self.request.user)


class ContactItem(generics.RetrieveUpdateDestroyAPIView, ContactPermission):
    permission_classes=[ContactPermission]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer       
