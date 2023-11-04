from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ambulanceRequest(models.Model):
    user = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)

class ambulanceLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def update_location(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.save()