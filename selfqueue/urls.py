from django.urls import path
from . import views

urlpatterns = [
      path('selfqueue/', views.book_spot, name='book_spot'),
      path('', views.results, name='results'),# For the main page
]
