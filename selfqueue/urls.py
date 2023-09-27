from django.urls import path
from . import views

urlpatterns = [
      path('selfqueue/', views.book_spot, name='book_spot'), # For the main page
]
