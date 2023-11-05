from django.urls import path
from . import views


urlpatterns = [
      path('selfqueue/', views.book_spot, name='book_spot'),
      path('', views.results, name='results'),
      path('feedback/', views.feedback, name='feedback'),# For the main page
      path('view_queue/', views.view_queue, name='view_queue'),
      path('selfqueue/feedback/<int:doctor_id>/', views.feedback, name='feedback'),
      path('writeReport/', views.writeReport, name='writeReport'),
      path('take-in/<int:id_number>/', views.take_in_patient, name='take_in_patient'),
      path('writeReport/<int:id_number>/', views.writeReport, name='writeReport'),
      path('get_patient_data/', views.get_patient_data, name='get_patient_data'),
      path('dashboard/', views.dashboard_view, name='dashboard'),
      path('export_data/', views.export_data, name='export_data'),
      path('get_symptom_data/', views.symptom_data, name='get_symptom_data'),
      path('patient_distribution_data/', views.patient_distribution_data, name='patient_distribution_data'),

      path('take-in/<int:spot_number>/', views.take_in_patient, name='take_in_patient'),
      path('writeReport/<int:spot_number>/', views.writeReport, name='writeReport'),
]
