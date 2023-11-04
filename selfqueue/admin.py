from django.contrib import admin
from .models import PatientQueue
from django.contrib import admin
from .models import Symptom # Import your models

# Register the Symptom model
class SymptomAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
class PatientQueueAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id_number', 'phone', 'spot_number','estimated_time','closing_time','status')
    list_filter = ('status',)
    search_fields = ('first_name', 'last_name', 'id_number', 'phone')

admin.site.register(PatientQueue, PatientQueueAdmin)
admin.site.register(Symptom, SymptomAdmin)
