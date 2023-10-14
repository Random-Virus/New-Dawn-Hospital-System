from django import forms
from .models import ambulanceRequest

class ambulanceRequestForm(forms.ModelForm):
    class Meta:
        model = ambulanceRequest
        fields = ['latitude', 'longitude']
