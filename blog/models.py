
from django.db import models
from django.contrib.auth.models import User  # If you want to associate articles with users

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

# Article Model
class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # If you want to associate articles with users
    date = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='article_images/')  # Define the upload path for article pictures

    def __str__(self):
        return self.title
