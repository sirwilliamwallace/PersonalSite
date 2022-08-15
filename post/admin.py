from django.contrib import admin
from .models import Post, PostCategory, PostTag, PostComment


@admin.register(Post)
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


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'url_title', 'isDelete', 'isActive',)
    search_fields = ('title', 'url_title',)


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ('caption', 'post',)
    list_filter = ('post',)
    search_fields = ('post',)


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('indicated_post', 'user', 'parent', 'createDate', 'isApproved',)
    list_filter = ('indicated_post', 'user', 'createDate', 'isApproved',)
    search_fields = ('indicated_post', 'user', 'comment_text',)
    list_editable = ('isApproved',)
