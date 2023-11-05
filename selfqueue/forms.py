from django import forms
from .models import PatientQueue, Symptom  # Import the PatientQueue and Symptom models
from .models import MedicalRecord
from django.utils import timezone 

from appointment.models import Doctor, Service
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['survey_question', 'rating', 'message']

    # Add Bootstrap styling to form elements
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['survey_question'].widget.attrs.update({'class': 'form-check-input'})
        self.fields['message'].widget.attrs.update({'class': 'form-control', 'rows': 6, 'placeholder': 'Any Comments or Complaints'})

        # Customize the rendering of the rating field
        self.fields['rating'].widget = forms.RadioSelect(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], attrs={'class': 'form-check-input'})
class MedicalRecordForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(
        queryset=Doctor.objects.all(),
        empty_label="Select a doctor",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )

    service = forms.ModelChoiceField(
        queryset=Service.objects.all(),
        empty_label="Select a service",
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )

    class Meta:
        model = MedicalRecord
        fields = [
            'doctor',
          
            'diagnosis',
            'prescription',
            'service',
            'date',
            'referrals',
            'further_examination',
        ]
        widgets = {
            'doctor': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
          
            'diagnosis': forms.Textarea(attrs={'class': 'form-control form-control-sm'}),
            'prescription': forms.Textarea(attrs={'class': 'form-control form-control-sm'}),
            'service': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'date': forms.DateInput(attrs={'class': 'form-control form-control-sm'}),
            'referrals': forms.Textarea(attrs={'class': 'form-control form-control-sm'}),
            'further_examination': forms.Textarea(attrs={'class': 'form-control form-control-sm'}),
        }

    def __init__(self, *args, **kwargs):
        super(MedicalRecordForm, self).__init__(*args, **kwargs)
        
        # Set the initial value for the date field to the current date
        self.fields['date'].initial = timezone.now().date()
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
