from django import forms
from .models import ambulanceRequest

class ambulanceRequestForm(forms.ModelForm):
    class Meta:
        model = ambulanceRequest
        fields = ['note', 'latitude', 'longitude']
    note = forms.CharField(
        label='Note',
        max_length=255,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Note'})
    )
    latitude = forms.FloatField(widget=forms.TextInput(attrs={'id': 'latitude', 'type': 'hidden'}))
    longitude = forms.FloatField(widget=forms.TextInput(attrs={'id': 'longitude', 'type': 'hidden'}))
    