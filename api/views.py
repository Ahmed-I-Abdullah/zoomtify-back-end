from rest_framework import generics
from meetings.models import Meeting, Contact
from .serializers import MeetingSerializer, ContactSerializer
from whatsappNotifier.scheduler import schedule_message
import threading

class MeetingList(generics.ListCreateAPIView):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer

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

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer   
