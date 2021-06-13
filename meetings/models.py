from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from users.models import User

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    phone_number = PhoneNumberField(unique=True)
    associated_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return (
            f'Contact: {self.first_name}, {self.phone_number}'
        )
        

class Meeting(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
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
