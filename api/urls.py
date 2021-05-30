from django.urls import path
from .views import MeetingList, ContactList

app_name = 'api'

urlpatterns = [
    path('', MeetingList.as_view(), name='meeting_listcreate'),
    path('contacts', ContactList.as_view(), name='contact_listcreate'),
]
