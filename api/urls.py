from django.urls import path
from .views import MeetingList, ContactList, MeetingItem, ContactItem

app_name = 'api'

urlpatterns = [
    path('meetings', MeetingList.as_view(), name='meeting_listcreate'),
    path('contacts', ContactList.as_view(), name='contact_listcreate'),
    path('meetings/<int:pk>/', MeetingItem.as_view(), name='meeting_detail'),
    path('contacts/<int:pk>/', ContactItem.as_view(), name='contact_detail'),
]
