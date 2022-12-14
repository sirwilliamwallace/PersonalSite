# Generated by Django 4.1 on 2022-08-07 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='', verbose_name='Avatar ')),
                ('name', models.CharField(max_length=100, verbose_name='Name ')),
                ('profile', models.CharField(max_length=100, verbose_name='Skills ')),
                ('email', models.EmailField(max_length=300, verbose_name='Email Address ')),
                ('phone', models.CharField(max_length=100, verbose_name='Phone Number')),
                ('about', models.TextField(null=True, verbose_name='About ')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': "Profile's",
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_image', models.ImageField(upload_to='back_ground_image/', verbose_name='Background Image')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Name')),
                ('skills', models.ManyToManyField(to='home.skills', verbose_name='Skills')),
            ],
            options={
                'verbose_name': 'Hero Section',
                'verbose_name_plural': 'Hero Section',
            },
        ),
    ]
