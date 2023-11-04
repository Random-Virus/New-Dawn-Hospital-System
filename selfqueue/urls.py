from django.urls import path
from . import views

urlpatterns = [
      path('selfqueue/', views.book_spot, name='book_spot'),
      path('', views.results, name='results'),
      path('feedback/', views.feedback, name='feedback'),# For the main page
      path('view_queue/', views.view_queue, name='view_queue'),
      path('update_patient_status/<int:id_number>/', views.update_patient_status, name='update_patient_status'),
]
