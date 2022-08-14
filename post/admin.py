from django.contrib import admin
from . import models


# Register your models here.
from .models import Post


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ('title', 'author', 'isActive',)
    list_filter = ('author', 'createDate', 'updateDate', 'isActive',)
    search_fields = ('title', 'description', 'content',)
    list_editable = ('isActive',)

    def save_model(self, request, obj: Post, form, change):
        if not change:
            obj.author = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)



@admin.register(models.PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_title', 'isDelete', 'isActive', 'parent_model')
    search_fields = ('title', 'url_title',)


@admin.register(models.PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ('caption', 'post',)
    list_filter = ('post',)
    search_fields = ('post',)
