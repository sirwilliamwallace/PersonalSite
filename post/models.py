from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    date = models.DateTimeField()
    isActive = models.BooleanField()
    content = models.TextField()
