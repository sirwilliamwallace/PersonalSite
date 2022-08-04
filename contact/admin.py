from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.ContactModel)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'full_name', 'createDate', 'isRead',)
    list_filter = ('isRead', 'createDate',)
    list_editable = ('isRead',)

