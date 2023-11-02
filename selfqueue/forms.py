from django import forms
from .models import PatientQueue, Symptom  # Import the PatientQueue and Symptom models

class BookingForm(forms.ModelForm):
    class Meta:
        model = PatientQueue
        fields = ['first_name', 'last_name', 'id_number', 'phone','symptoms']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID Number'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }
    symptoms = forms.ModelMultipleChoiceField(
        queryset=Symptom.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,  # This allows no symptom to be selected if desired
    )

   
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if any(char.isdigit() or not char.isalnum() for char in first_name):
            raise forms.ValidationError("First name must not contain numbers or special characters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if any(char.isdigit() or not char.isalnum() for char in last_name):
            raise forms.ValidationError("Last name must not contain numbers or special characters.")
        return last_name

    def clean_id_number(self):
        id_number = self.cleaned_data.get('id_number')
        if not id_number.isdigit() or len(id_number) != 13:
            raise forms.ValidationError("ID number must be 13 digits and contain only numbers.")
        return id_number
