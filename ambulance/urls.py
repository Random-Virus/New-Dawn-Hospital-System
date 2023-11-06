from django.urls import path
from . import views

urlpatterns = [
    path('', views.ambulanceRequestView, name='ambulanceRequest'),
    path('find_nearest_hospital/', views.find_nearest_hospital, name='hospital_nearest'),
    path('view_requests/', views.viewRequests, name='view_requests'),
    path('request_detail/<int:request_id>', views.request_detail, name='request_details'),
    # path('get_ambulance_requests_data/', views.get_ambulance_requests_data, name='get_ambulance_requests_data'),
    path('dashboard/', views.dashboard, name='dashboard-ambulance'),
    path('ambulance_request_count/', views.ambulance_request_count, name='ambulance_request_count'),
    # path('get_hospital_locations/', views.hospital_locations, name='get_hospital_locations'),
    # path('map/', views.map, name='map'),
    # path('heatmap-data/', views.heatmap_data, name='heatmap-data'),
]