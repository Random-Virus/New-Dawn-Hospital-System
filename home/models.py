from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)
    id_number = models.CharField(max_length=16, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    medical_aid = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    def full_address(self):
        address_parts = [self.address, self.city, self.state, self.zip, self.country]
        address_parts = [part for part in address_parts if part]  # Remove empty parts
        return ", ".join(address_parts)

    def save(self, *args, **kwargs):
        # Update User model's first_name, last_name, and email fields based on name and surname
        if self.user:
            self.user.first_name = self.name
            self.user.last_name = self.surname
            self.user.email = self.email
            self.user.save()
        super(Profile, self).save(*args, **kwargs)
