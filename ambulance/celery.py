from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Define a periodic task to update locations every minute
app.conf.beat_schedule = {
    'update-locations': {
        'task': 'ambulance.tasks.update_location_task',
        'schedule': crontab(minute='*'),  # Run every minute
    },
}
