from django.urls import path , include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appointment/', views.appointment, name='appointment'),
   path('selfqueue/', include('selfqueue.urls')),
   path('blog/', views.blog, name='blog'),
]