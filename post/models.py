from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    author = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    isActive = models.BooleanField(default=False)
    content = models.TextField()

    def __str__(self):
        return self.title
