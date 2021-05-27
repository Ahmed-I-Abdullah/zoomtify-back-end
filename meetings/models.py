from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)

class Meeting(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_time = models.DateField()
    



