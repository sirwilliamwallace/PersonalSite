from django.contrib import admin
from .models import Hero, Skills


# Register your models here.
@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    pass


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    pass
