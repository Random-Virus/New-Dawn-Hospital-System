from django import forms

from .models import Doctor, Service
from .models import Appointment
from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.core.exceptions import ValidationError

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'phone', 'email', 'service', 'note']
    first_name = forms.CharField(
        label='Name',
        max_length=120,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'})
    )
    last_name = forms.CharField(
        label='Surname',
        max_length=120,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Surname'})
    )
    phone = forms.CharField(
        label='Phone Number',
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'})
    )
    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address'})
    )
    note = forms.CharField(
        label='Note',
        max_length=255,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Note'})
    )

    service = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        empty_label="Select a service",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class confirmForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time']

    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        empty_label="Select a doctor",
        widget=forms.Select(attrs={'class': 'form-control'}), 
        required=True
    )
    date = forms.DateField(
        label='Date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=True
    )
    time = forms.TimeField(
        label='Time',
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        required=True
    )
