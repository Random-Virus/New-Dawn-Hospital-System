from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.title


class Doctor(models.Model):
    name = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)
    picture = models.ImageField(upload_to="media/doctors/")
    details = models.TextField()
    experience = models.TextField()
    expertize = models.CharField(max_length=120)
    twitter = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name
class Appointment(models.Model):

    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    note = models.TextField(blank=True)
    request_number = models.CharField(max_length=10, default=get_random_string(length=10), unique=True)
    request_date = models.DateTimeField(default=timezone.now)