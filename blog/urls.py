from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name='blog'), # For the main page
    path('blog/<int:article_id>/', views.blog_details, name='blog_details'),
    path('search/', views.search_articles, name='search_articles'),
    path('category/<int:category_id>/', views.category_articles, name='category_articles'),
    path('editor/', views.editor, name='editor'),
]
