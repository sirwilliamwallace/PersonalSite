from django.contrib import admin
from .models import Hero, Skills, SiteSettings, Profile


# Register your models here.
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    pass


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    pass


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
