from django.contrib import admin
from .models import Article, Category  # Import your models

# Register the Article model
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'date')
    list_filter = ('category', 'author', 'date')
    search_fields = ('title', 'content')
  

# Register the Category model
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
