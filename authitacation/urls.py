from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'), # For the main page
    path('login/', views.login_view, name='login'),
    
]
