from django.contrib import admin
from .models import ambulanceRequest, Hospital

class ambulanceRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'latitude', 'longitude', 'timestamp')


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude')

admin.site.register(ambulanceRequest, ambulanceRequestAdmin)
admin.site.register(Hospital, HospitalAdmin)
