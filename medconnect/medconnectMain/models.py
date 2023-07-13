from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ["-sent_date"]


class Doctor(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    name = models.CharField(max_length=60)
    mobile = PhoneNumberField(
            max_length=20,
            blank=True,
            null=True,
            help_text="Enter a valid WhatsApp phone number in the format +1234567890123"
        )
    special = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name