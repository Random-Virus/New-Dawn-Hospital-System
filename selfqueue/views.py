from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking
from datetime import datetime, timedelta
from django.utils import timezone
def book_spot(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)

            # Calculate the spot number and estimated time based on the last booking
            last_booking = Booking.objects.last()
            if last_booking:
                last_estimated_time = last_booking.estimated_time
                # Calculate the estimated time for the new booking (e.g., 15 minutes from the last person)
                booking.estimated_time = last_estimated_time + timedelta(minutes=15)
                # Calculate the spot number by incrementing the last person's spot number
                last_spot_number = last_booking.spot_number
                booking.spot_number = str(int(last_spot_number) + 1)
            else:
                # If there are no previous bookings, start from 1 and set the estimated time (e.g., 15 minutes from now)
                booking.spot_number = '1'
                booking.estimated_time = datetime.now() + timedelta(minutes=15)

            # Determine the status
            current_time = datetime.now()
            if current_time < booking.estimated_time:
                booking.status = 'Awaiting Consultation'
            else:
                booking.status = 'In Consultation'

            booking.save()  # Save the booking after all calculations

            return render(request, 'booking_confirmation.html', {'booking': booking})

    else:
        form = BookingForm()

    return render(request, 'selfqueue/index.html', {'form': form})
