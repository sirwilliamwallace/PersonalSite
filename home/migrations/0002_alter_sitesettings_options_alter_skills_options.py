# Generated by Django 4.1 on 2022-08-08 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesettings',
            options={'verbose_name': 'Settings', 'verbose_name_plural': 'Settings'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'Skill', 'verbose_name_plural': 'Skills Section'},
        ),
    ]
