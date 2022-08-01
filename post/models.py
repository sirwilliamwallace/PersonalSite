from django.db import models
import os

from django.urls import reverse
from django.utils.text import slugify


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    author = models.OneToOneField() #TODO: inherit user table
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=False)
    content = models.TextField(default="", null=False, db_index=True)

    def get_absolute_url(self):
        return reverse('post-detail', args=[
            self.id, self.title
        ])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

