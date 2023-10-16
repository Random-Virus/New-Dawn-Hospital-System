from django.urls import path , include
from django.conf.urls.i18n import set_language
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('profile_view/', views.profile_view, name='profile_view'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('i18n/', set_language, name='set_language'),

    path('selfqueue/', include('selfqueue.urls')),
    path('blog/', views.blog, name='blog'),
]