# Generated by Django 4.1 on 2022-08-14 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postcategory',
            name='parent_model',
        ),
    ]
