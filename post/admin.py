from django.contrib import admin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ('title', 'author', 'isActive',)
    list_filter = ('author', 'createDate', 'updateDate', 'isActive',)
    search_fields = ('title', 'description', 'content',)
    list_editable = ('isActive',)
