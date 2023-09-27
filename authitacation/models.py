from django.db import models




class patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)