# Generated by Django 4.1 on 2022-08-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_socialmediaaccounts_getintouch'),
    ]

    operations = [
        migrations.AddField(
            model_name='getintouch',
            name='isActive',
            field=models.BooleanField(default=False, verbose_name='Be shown in contact section'),
        ),
    ]
