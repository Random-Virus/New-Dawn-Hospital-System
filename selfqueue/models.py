from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    symptoms = models.TextField()
    spot_number = models.CharField(max_length=10)
    estimated_time = models.DateTimeField(null=True)
    status = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        # Calculate the spot number and estimated time based on the last booking
        last_booking = Booking.objects.last()
        if last_booking:
            last_estimated_time = last_booking.estimated_time
            # Calculate the estimated time for the new booking (e.g., 15 minutes from the last person)
            self.estimated_time = last_estimated_time + timedelta(minutes=15)
            # Calculate the spot number by incrementing the last person's spot number
            last_spot_number = last_booking.spot_number
            self.spot_number = str(int(last_spot_number) + 1)
        else:
            # If there are no previous bookings, start from 1 and set the estimated time (e.g., 15 minutes from now)
            self.spot_number = '1'
            self.estimated_time = datetime.now() + timedelta(minutes=15)

        # Determine the status
        current_time = datetime.now()
        if current_time < self.estimated_time:
            self.status = 'Awaiting Consultation'
        else:
            self.status = 'In Consultation'

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking for {self.first_name} {self.last_name}"
