from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    phone_number = PhoneNumberField(unique=True)

    def clean(self):
        if not self.phone_number:
            raise ValidationError('Phone number is required.')

        super().clean()

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    phone_number = PhoneNumberField(unique=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return (
            f'Contact: {self.first_name}, {self.phone_number}'
        )
        

class Meeting(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    start_date_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    message = models.CharField(max_length=255)
    notified_contacts = models.ManyToManyField(Contact, related_name='notification_meetings')

    class Meta:
        get_latest_by = 'start_date_time'
        ordering = ['start_date_time']
        verbose_name = 'Meeting'
        verbose_name_plural = 'Meetings'

    def __str__(self):
        return (
            f'Meeting: {self.name}, {self.start_date_time}'
        )    
