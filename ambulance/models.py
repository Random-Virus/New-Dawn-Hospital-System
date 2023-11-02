from django.db import models

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
