from django.contrib.auth.models import User
from django.db import models


class Hero(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Name')
    skills = models.ManyToManyField('Skills', verbose_name='Skills')
    bg_image = models.ImageField(verbose_name='Background Image', upload_to='back_ground_image/')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Hero Section'
        verbose_name_plural = 'Hero Section'


class Skills(models.Model):
    skill = models.CharField(max_length=50)
    short_description = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f"{self.skill}"


class SiteSettings(models.Model):
    logo = models.ImageField()
