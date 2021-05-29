from django.urls import path
from .views import MeetingList

app_name = 'api'

urlpatterns = [
    path('', MeetingList.as_view(), name="listcreate")
]
