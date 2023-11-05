from django.urls import path
from . import views

urlpatterns = [
      path('selfqueue/', views.book_spot, name='book_spot'),
      path('', views.results, name='results'),
      path('feedback/', views.feedback, name='feedback'),# For the main page
      path('view_queue/', views.view_queue, name='view_queue'),
      path('writeReport/', views.writeReport, name='writeReport'),
      path('take-in/<int:id_number>/', views.take_in_patient, name='take_in_patient'),
      path('writeReport/<int:id_number>/', views.writeReport, name='writeReport'),
]
