from django.contrib import admin
from .models import ambulanceRequest, Hospital, ambulanceLocation

class ambulanceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'latitude', 'longitude', 'timestamp')


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')

class ambulanceLocationAdmin(admin.ModelAdmin):
    list_display = ('user', 'latitude', 'longitude')

admin.site.register(ambulanceRequest, ambulanceRequestAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(ambulanceLocation, ambulanceLocationAdmin)
