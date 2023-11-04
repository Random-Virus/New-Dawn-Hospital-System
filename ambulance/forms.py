from django import forms
from .models import ambulanceRequest

class ambulanceRequestForm(forms.ModelForm):
    class Meta:
        model = ambulanceRequest
        fields = ['note', 'latitude', 'longitude']

    latitude = forms.FloatField(widget=forms.TextInput(attrs={'id': 'latitude', 'type': 'hidden'}))
    longitude = forms.FloatField(widget=forms.TextInput(attrs={'id': 'longitude', 'type': 'hidden'}))
    