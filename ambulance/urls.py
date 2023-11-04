from django.urls import path
from . import views

urlpatterns = [
    path('', views.ambulanceRequestView, name='ambulanceRequest'),
    path('find_nearest_hospital/', views.find_nearest_hospital, name='hospital_nearest'),
    path('view_requests/', views.viewRequests, name='view_requests'),
    path('request_detail/<int:request_id>', views.request_detail, name='request_details')
]