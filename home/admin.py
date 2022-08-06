from django.contrib import admin
from .models import Hero, Skills, SiteSettings


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
