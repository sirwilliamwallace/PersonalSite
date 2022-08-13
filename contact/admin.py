from django.contrib import admin
from .models import ContactModel
from home.models import GetInTouch, SocialMediaAccounts

# Register your models here.
@admin.register(ContactModel)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('title', 'email', 'full_name', 'createDate', 'isRead',)
    list_filter = ('isRead', 'createDate',)
    list_editable = ('isRead',)


@admin.register(GetInTouch)
class ContactFormAdmin(admin.ModelAdmin):
    pass


@admin.register(SocialMediaAccounts)
class ContactFormAdmin(admin.ModelAdmin):
    pass
