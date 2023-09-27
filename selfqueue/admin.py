from django.contrib import admin
from .models import Booking  # Import your Booking model

class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'id_number', 'phone', 'spot_number', 'estimated_time', 'status')
    list_filter = ('status',)
    search_fields = ('first_name', 'last_name', 'id_number', 'phone', 'status')

# Register your model with the custom admin class
admin.site.register(Booking, BookingAdmin)
