from django.shortcuts import render, redirect
from .forms import AppointmentForm, confirmForm
from .models import Appointment
from django.core.mail import send_mail
#import settings
from django.conf import settings
from django.shortcuts import get_object_or_404
#import jsonrespone
from django.http import JsonResponse
from datetime import datetime, timedelta

# Create your views here.
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
       
        if form.is_valid():
            form.save()
            print(form.errors)
            print('Error')
            return redirect('confirmation') 
    else:
        form = AppointmentForm()
        
    context = {
        'form': form,
       
        }
    return render(request, 'appointment/appointment.html', context)
def confirmation_view(request):
    return render(request, 'appointment/confirmation.html')
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
            subject = 'Appointment Confirmation at New Dawn Hospital'
            message = f'Dear {appointments.first_name} {appointments.last_name},\n\n' \
                  f'Your appointment at New Dawn Hospital has been confirmed. Here are the details:\n\n' \
                  f'Doctor: { appointments.doctor}\n' \
                  f'Date: {appointments.date}\n' \
                  f'Time: {appointments.time}\n\n' \
                  f'Thank you for choosing New Dawn Hospital for your medical needs.\n' \
                  f'We look forward to seeing you on the scheduled date.\n\n' \
                  f'Best regards,\n' \
                  f'New Dawn Hospital Team'

            from_email = settings.EMAIL_HOST_USER
            to_email = appointments.email

            send_mail(subject, message, from_email, [to_email])\
            
            return redirect('view_appointments')
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
        subject = 'Appointment Confirmation at New Dawn Hospital'
        message = f'Dear {appointments.first_name} {appointments.last_name},\n\n' \
                  f'Your appointment at New Dawn Hospital has been confirmed. Here are the details:\n\n' \
                  f'Doctor: {doctor.name}\n' \
                  f'Date: {appointments.date}\n' \
                  f'Time: {appointments.time}\n\n' \
                  f'Thank you for choosing New Dawn Hospital for your medical needs.\n' \
                  f'We look forward to seeing you on the scheduled date.\n\n' \
                  f'Best regards,\n' \
                  f'New Dawn Hospital Team'

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

def dashboard(request):
    return render(request, 'appointment/dashboard.html')


def confirmation_rate_view(request):
    confirmed = Appointment.objects.filter(is_confirmed=True).count()
    total = Appointment.objects.count()
    
    confirmation_rate = (confirmed / total) * 100
    
    data = {
        "confirmed": confirmed,
        "total": total,
        "confirmation_rate": confirmation_rate,
    }
    print("Confirmation rate: ", confirmation_rate)
    return JsonResponse(data)

def waitlist_management_view(request):
    # Define the time periods you want to analyze (e.g., days or weeks)
    time_periods = []
    waitlist_counts = []

    # Define the start date and end date for the analysis
    start_date = datetime(2023, 1, 1)  # Replace with your desired start date
    end_date = datetime(2023, 12, 31)  # Replace with your desired end date

    current_date = start_date
    while current_date <= end_date:
        next_date = current_date + timedelta(days=1)  # You can adjust the interval as needed

        # Count the number of patients on the waitlist for the current time period
        waitlist_count = Appointment.objects.filter(
            date__gte=current_date, date__lt=next_date
        ).count()

        # Add the data to the lists
        time_periods.append(current_date.strftime('%Y-%m-%d'))  # Format the date as needed
        waitlist_counts.append(waitlist_count)

        current_date = next_date

    data = {
        "timePeriods": time_periods,
        "waitlistCounts": waitlist_counts,
    }
    print(data)
    return JsonResponse(data)

def scheduling_patterns_view(request):
    # Define the time periods you want to analyze (e.g., days or weeks)
    time_periods = []
    appointment_counts = []

    # Define the start date and end date for the analysis
    start_date = datetime(2023, 1, 1)  # Replace with your desired start date
    end_date = datetime(2023, 12, 31)  # Replace with your desired end date

    current_date = start_date
    while current_date <= end_date:
        next_date = current_date + timedelta(days=1)  # You can adjust the interval as needed

        # Count the number of appointments scheduled for the current time period
        appointment_count = Appointment.objects.filter(
            date__gte=current_date, date__lt=next_date
        ).count()

        # Add the data to the lists
        time_periods.append(current_date.strftime('%Y-%m-%d'))  # Format the date as needed
        appointment_counts.append(appointment_count)

        current_date = next_date

    data = {
        "timePeriods": time_periods,
        "appointmentCounts": appointment_counts,
    }

    return JsonResponse(data)