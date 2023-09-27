from django import forms
from .models import Booking  # Import the Booking model

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'id_number', 'phone', 'symptoms']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID Number'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'symptoms': forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Possible Symptoms'}),
        }
