from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Q

User = get_user_model()

#  Search functionality for posts


class PostManager(models.Manager):
    def get_active_posts(self):
        query_set = self.get_queryset().filter(isActive=True)
        return query_set
    def search(self, query):
        lookup = (
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__username__icontains=query) |
            Q(slug__icontains=query) |
            Q(description__icontains=query) |
            Q(category__title__icontains=query) |
            Q(category__url_title__icontains=query)
        )
        return self.get_queryset().filter(lookup, isActive=True).distinct()


class Post(models.Model):
    title = models.CharField(max_length=300,
                             unique=True,
                             verbose_name='Title'
                             )
    category = models.ManyToManyField('PostCategory',
                                      related_name='post_categories',
                                      verbose_name='Categories'
                                      )
    slug = models.SlugField(max_length=300,
                            default="", null=False,
                            db_index=True,
                            unique=True,
                            verbose_name='Slug (Auto-complete)'
                            )
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts',
                               verbose_name='Author',
                               editable=False
                               )
    description = models.CharField(max_length=300,
                                   verbose_name='Short Description'
                                   )
    content = RichTextUploadingField(verbose_name='Content')
    createDate = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Created Date')
    updateDate = models.DateTimeField(auto_now=True,
                                      verbose_name='Updated Date')
    image = models.ImageField(upload_to='post_images/',
                              null=True,
                              blank=True,
                              verbose_name='Image',
                              )
    isActive = models.BooleanField(default=False,
                                   verbose_name='Active / Inactive')
    isDelete = models.BooleanField(verbose_name='Deleted')

    objects = PostManager()

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
    caption = models.CharField(max_length=300,
                               db_index=True,
                               verbose_name='Caption')
    post = models.ForeignKey('Post',
                             on_delete=models.CASCADE,
                             related_name='post_tags',
                             verbose_name='Post')

    class Meta:
        verbose_name = "Post's tag"
        verbose_name_plural = "Post's tag"

    def __str__(self):
        return self.caption


class PostCategory(models.Model):
    title = models.CharField(max_length=300,
                             db_index=True,
                             verbose_name='Title')
    url_title = models.CharField(max_length=300,
                                 db_index=True,
                                 verbose_name='Url Title')
    isActive = models.BooleanField(default=False,
                                   verbose_name='Active / Inactive')
    isDelete = models.BooleanField(verbose_name='Deleted')

    def __str__(self):
        return f"{self.title} - {self.url_title}"

    class Meta:
        verbose_name = 'Post Category'
        verbose_name_plural = "Post Categories"


class PostComment(models.Model):
    indicated_post = models.ForeignKey(Post,
                                       related_query_name='posts',
                                       on_delete=models.CASCADE, verbose_name="Post ")
    parent = models.ForeignKey('PostComment',
                               db_index=True,
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE,
                               related_name='parents',
                               verbose_name='Parent comment')
    user = models.ForeignKey(User,
                             db_index=True,
                             on_delete=models.CASCADE,
                             verbose_name='User ')
    createDate = models.DateTimeField(db_index=True,
                                      auto_now_add=True,
                                      verbose_name='Create Date')
    isApproved = models.BooleanField(default=False,
                                     verbose_name='Is Approved')
    comment_text = models.TextField(db_index=True,
                                    verbose_name='Text ')

    def __str__(self):
        return f"{self.indicated_post.title} - {self.user}"

    class Meta:
        verbose_name = "Comments"
        verbose_name_plural = "Comment"
