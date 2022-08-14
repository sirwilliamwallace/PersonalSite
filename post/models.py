from django.db import models
import os
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True, verbose_name='Title')
    category = models.ManyToManyField('PostCategory', related_name='post_categories', verbose_name='Categories')
    slug = models.SlugField(max_length=300, default="", null=False, db_index=True, unique=True,
                            verbose_name='Slug (Auto-complete)')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Author')
    description = models.CharField(max_length=300, verbose_name='Short Description')
    content = RichTextUploadingField(verbose_name='Content')
    createDate = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')
    updateDate = models.DateTimeField(auto_now=True, verbose_name='Updated Date')
    image = models.ImageField(upload_to=f'post_images/', null=True,blank=True, verbose_name='Image')
    isActive = models.BooleanField(default=False, verbose_name='Active / Inactive')
    isDelete = models.BooleanField(verbose_name='Deleted')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post-detail', args=[str(self.id), self.slug])

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
    parent_model = models.ForeignKey('PostCategory',
                                     on_delete=models.CASCADE,
                                     verbose_name="Parent Category",
                                     null=True,
                                     blank=True
                                     )
    title = models.CharField(max_length=300, db_index=True, verbose_name='Title')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='Url Title')
    isActive = models.BooleanField(default=False, verbose_name='Active / Inactive')
    isDelete = models.BooleanField(verbose_name='Deleted')

    def __str__(self):
        return f"{self.title} - {self.url_title}"

    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = "Post Categories"
