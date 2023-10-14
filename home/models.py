from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    id_number = models.CharField(max_length=16)
    date_of_birth = models.DateField()
    medical_aid = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


    def save(self, *args, **kwargs):
        # Update User model's first_name and last_name fields based on name and surname
        if self.user:
            self.user.first_name = self.name
            self.user.last_name = self.surname
            self.user.email = self.email
            self.user.save()
        super(profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
        
    def full_name(self):
        return f"{self.name} {self.surname}"

    def full_address(self):
        return f"{self.address}, {self.city}, {self.state}, {self.zip}, {self.country}"