from django.db import models
import os
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(default="", null=False, db_index=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=False)
    content = RichTextUploadingField()

    def get_absolute_url(self):
        return reverse('post-detail', args=[
            self.id, self.title
        ])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
