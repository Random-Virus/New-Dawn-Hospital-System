from django.db import models
from django.contrib.auth.models import User  # Im
class Symptom(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PatientQueue(models.Model):
    STATUS_CHOICES = (
        ('Awaiting Consultation', 'Awaiting Consultation'),
        ('In Consultation', 'In Consultation'),
        ('Done with Consultation', 'Done with Consultation'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Define the foreign key
    symptoms = models.ManyToManyField(Symptom, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=15, unique=True)
    phone = models.CharField(max_length=15)

    estimated_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Awaiting Consultation')
    closing_time = models.DateTimeField(null=True, blank=True)
    spot_number = models.IntegerField(unique=True)  # New field for spot number

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
