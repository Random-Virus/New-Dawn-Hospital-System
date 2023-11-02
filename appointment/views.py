from django.shortcuts import render, redirect
from .forms import AppointmentForm, confirmForm
from .models import Appointment
from django.core.mail import send_mail
#import settings
from django.conf import settings
from django.shortcuts import get_object_or_404
# Create your views here.
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
       
        if form.is_valid():
            form.save()
            print(form.errors)
            print('Error')
            return redirect('index') 
    else:
        form = AppointmentForm()
        
    context = {
        'form': form,
       
        }
    return render(request, 'appointment/appointment.html', context)

def view_appointments(request):
    appointments = Appointment.objects.filter(is_confirmed=False)
    
    context = {
        'appointments': appointments,
        
        }
    return render(request, 'appointment/view_appointments.html', context)

def appointment_details(request, request_number):
    appointments = get_object_or_404(Appointment, request_number=request_number)

    if request.method == 'POST':
        form = confirmForm(request.POST)
        if form.is_valid():
            appointments.doctor = form.cleaned_data['doctor']
            appointments.date = form.cleaned_data['date']
            appointments.time = form.cleaned_data['time']
            appointments.is_confirmed = True
            appointments.save()
            print('Appointments saved')
            subject = 'Appointments confirmed'
            message = f'Your appointment has been confirmed'
            from_email = settings.EMAIL_HOST_USER
            to_email = appointments.email

            send_mail(subject, message, from_email, [to_email])
    else:
        form = confirmForm()
        print('Appointments not saved')
    context = {
        'form': form,
        'appointments': appointments
        }
    
    return render(request, 'appointment/appointment_details.html', context)


def confirm_appointment(request, request_number):
    appointments = get_object_or_404(Appointment, request_number=request_number)
    if 'doctor' in request.POST:
        doctor_id = request.POST.get('doctor')
        doctor = get_object_or_404(Doctor, id=doctor_id)

        appointments.doctor = doctor
        appointments.date = request.POST.get('date')
        appointments.time = request.POST.get('time')
        appointments.save()
        print('Appointments saved')
        #send an email to the user to confirm the appointment
        subject = 'Appointments confirmed'
        message = f'Your appointment has been confirmed'
        from_email = settings.EMAIL_HOST_USER
        to_email = appointments.email

        try:
            send_mail(subject, message, from_email, [to_email])
            print("Email sent")
        except Exception as e:
            print(e)
            print(f"Failed to send email to {to_email}: {e}")
        #send_mail(subject, message, from_email, to_list, fail_silently=True)

    else:
        print("Two")
    messages.success(request, 'Appointment confirmed successfully!')
    return redirect('view_appointments')

def send_twilio_message(appointment):
    account_sid = 'AC810660139ff7571863cbf97b8f6b0e21'
    auth_token = '51b59aab2bdfb9ddbc4dc44f96b90fb6'
    client = Client(account_sid, auth_token)
    number = patient.phone
    message_body = f"Hello, you have successfully reserved your place at New Dawn Hospital. Patient Name: {patient.first_name} {patient.last_name}, Spot Number: {patient.spot_number}, Predicted Consultation Time: {patient.estimated_time}. Please be informed that our scheduling system is subject to the availability of our medical professionals and other operational considerations."
    message = client.messages.create(
        body=message_body,
        from_='+14143770567',
        to='+27810207623'
    )