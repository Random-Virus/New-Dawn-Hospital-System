from django.db import models
from appointment.models import Doctor
from django.contrib.auth.models import User  # Im
class Feedback(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    survey_question = models.CharField(max_length=3, choices=[('yes', 'Yes'), ('no', 'No')])
    rating = models.PositiveIntegerField()
    message = models.TextField()
    
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

class PatientQueueHistory(models.Model):
    user = models.CharField(max_length=100)
    symptoms = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    estimated_time = models.DateTimeField()
    status = models.CharField(max_length=50)
    closing_time = models.DateTimeField()
    spot_number = models.IntegerField()


    
class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientQueue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    prescription = models.TextField()
    service = models.CharField(max_length=100)
    date = models.DateField()
    referrals = models.TextField(blank=True)
    further_examination = models.TextField(blank=True)

    def __str__(self):
        return f"Medical Record for {self.patient.first_name} {self.patient.last_name}"
class PatientQueueHistory(models.Model):
    user = models.CharField(max_length=100)
    symptoms = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    estimated_time = models.DateTimeField()
    status = models.CharField(max_length=50)
    closing_time = models.DateTimeField()
    spot_number = models.IntegerField()