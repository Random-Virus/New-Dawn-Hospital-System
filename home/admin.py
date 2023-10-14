from django.contrib import admin
from .models import profile
# Register your models here.


class profileAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'phone', 'id_number', 'date_of_birth', 'address', 'city', 'state', 'zip', 'country')
    list_filter = ('name', 'surname', 'email', 'phone', 'id_number', 'date_of_birth', 'address', 'city', 'state', 'zip', 'country')
    search_fields = ('name', 'surname', 'email', 'phone', 'id_number', 'date_of_birth', 'address', 'city', 'state', 'zip', 'country')
    ordering = ['name']

admin.site.register(profile, profileAdmin)