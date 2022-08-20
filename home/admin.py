from django.contrib import admin

from .models import Hero, Skills, SiteSettings, Profile, Seo, Keywords, IpLog


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


@admin.register(Seo)
class SeoAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'isMain',)
    list_editable = ('isMain',)


@admin.register(Keywords)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'keyword',)


@admin.register(IpLog)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
