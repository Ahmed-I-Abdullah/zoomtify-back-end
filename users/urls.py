from django.urls import path
from .views import CreateUser, LogoutAndBlackList

app_name = 'users'

urlpatterns = [
    path('signup/', CreateUser.as_view(), name="signup"),
    path('blacklist/', LogoutAndBlackList.as_view(), name='blacklist')
]
