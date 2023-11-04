from celery import shared_task
from your_app.models import ambulanceLocation

@shared_task
def update_location_task(user_id, latitude, longitude):
    try:
        user_location = ambulanceLocation.objects.get(user_id=user_id)
        user_location.update_location(latitude, longitude)
    except ambulanceLocation.DoesNotExist:
        ambulanceLocation.objects.create(user_id=user_id, latitude=latitude, longitude=longitude)
