from django.urls import path
from . import views

urlpatterns = [
    path('appointment/', views.appointment, name='appointment'), # For the main page
    path('view_appointments/', views.view_appointments, name='view_appointments'),
      path('confirmation/', views.confirmation_view, name='confirmation'),
     path('appointment_details/<str:request_number>/', views.appointment_details, name='appointment_details'),
    path('confirm_appointment/<str:request_number>/', views.confirm_appointment, name='confirm_appointment'),
]
