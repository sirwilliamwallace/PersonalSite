from django.db import models
import os
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, default="", null=False, db_index=True, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    description = models.CharField(max_length=300)
    content = RichTextUploadingField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[
            self.id, self.title
        ])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-createDate']


class PostTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='Caption')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_tags', verbose_name='Post')

    class Meta:
        verbose_name = "Post's tag"
        verbose_name_plural = "Post's tag"

    def __str__(self):
        return self.caption


class PostCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='Title')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='Url Title')
    isActive = models.BooleanField(default=False, verbose_name='Active / Inactive')
    isDelete = models.BooleanField(verbose_name='Deleted')

    def __str__(self):
        return f"( {self.title} - {self.url_title} )"

    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = "Post Categories"
