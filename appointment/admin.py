from django.contrib import admin

# Register your models here.

#create admin for all models
from .models import Appointment, Service, Doctor
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title', 'description')
    search_fields = ('title', 'description')
    ordering = ['title']

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'speciality', 'picture', 'details', 'experience', 'expertize', 'twitter', 'facebook', 'instagram')
    list_filter = ('name', 'speciality', 'picture', 'details', 'experience', 'expertize', 'twitter', 'facebook', 'instagram')
    search_fields = ('name', 'speciality', 'picture', 'details', 'experience', 'expertize', 'twitter', 'facebook', 'instagram')
    ordering = ['name']

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'service', 'doctor', 'date', 'time', 'note', 'request_number', 'request_date')
    list_filter = ('first_name', 'last_name', 'email', 'phone', 'service', 'doctor', 'date', 'time', 'note', 'request_number', 'request_date')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'service', 'doctor', 'date', 'time', 'note', 'request_number', 'request_date')
    ordering = ['first_name']

admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Doctor, DoctorAdmin)