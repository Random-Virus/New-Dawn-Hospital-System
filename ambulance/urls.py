from django.urls import path
from . import views

urlpatterns = [
    path('', views.ambulanceRequestView, name='ambulanceRequest'),
    path('find_nearest_hospital/', views.find_nearest_hospital, name='hospital_nearest'),
    
]