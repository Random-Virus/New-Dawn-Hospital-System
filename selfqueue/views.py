import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import BookingForm
from .models import PatientQueue
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from django.urls import reverse
from twilio.rest import Client
from django.contrib.auth.models import User

from django.db.models import Max

# Configure the logging settings
logger = logging.getLogger(__name__)
@login_required
def book_spot(request):
    user = request.user  # Get the currently logged-in user

    # Check if the user already has a booking
    existing_booking = PatientQueue.objects.filter(user=user).first()

    if existing_booking:
        # If the user already has a booking, check the status
        if existing_booking.status == 'Done with Consultation':
           existing_booking.delete() # Delete the existing booking
           return HttpResponseRedirect(reverse('book_spot'))  # Redirect to 'selfqueue:index' URL
        else:
           return HttpResponseRedirect(reverse('results'))  # Redirect to 'results' URL

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)

            # Calculate estimated time, set status, and other necessary actions
            booking.estimated_time = get_estimated_time()
            booking.status = 'Awaiting Consultation'
            booking.closing_time = booking.estimated_time + timedelta(minutes=10)

            # Assign a spot number, save, and send a Twilio message
            assign_spot_number(booking)
            booking.user = user  # Associate the booking with the logged-in user

          
            booking.save()

            # Handle symptoms and duration
            symptoms = form.cleaned_data.get('symptoms')
            duration = form.cleaned_data.get('duration')
            booking.symptoms.set(symptoms)  
            booking.duration = duration   

            send_twilio_message(booking)

            return HttpResponseRedirect(reverse('results'))
    else:
        form = BookingForm()

    return render(request, 'selfqueue/index.html', {'form': form})
@login_required
def results(request):
    user = request.user

    try:
        patient = PatientQueue.objects.get(user=user)
        first_name = patient.first_name
        last_name = patient.last_name
        estimated_time = patient.estimated_time
        spot_number = patient.spot_number
        status = patient.status
    except PatientQueue.DoesNotExist:
        first_name = ""
        last_name = ""
        estimated_time = None
        spot_number = None
        status = ""

    return render(request, 'selfqueue/results.html', {
        'user': user,
        'first_name': first_name,
        'last_name': last_name,
        'estimated_time': estimated_time,
        'spot_number': spot_number,
        'status': status,
    })

# Other functions
def get_estimated_time():
    last_patient = PatientQueue.objects.last()
    if last_patient:
        return last_patient.closing_time
    else:
        return datetime.now()

def assign_spot_number(patient):
    last_spot_number = PatientQueue.objects.aggregate(Max('spot_number'))
    if last_spot_number['spot_number__max'] is not None:
        patient.spot_number = last_spot_number['spot_number__max'] + 1
    else:
        patient.spot_number = 1

def send_twilio_message(patient):
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

def feedback(request):
    return render(request, 'selfqueue/feedback.html')

def view_queue(request):
    patients = PatientQueue.objects.all()  # Retrieve all PatientQueue objects


    context = {
        'patients': patients,
       
    }
    return render(request, 'selfqueue/view_queue.html', context)
def update_patient_status(request, id_number):
    patient = get_object_or_404(PatientQueue, pk=id_number)
    patient.status = 'In Consultation'
    patient.save()
    return JsonResponse({'message': 'Status updated successfully'})