# Generated by Django 4.1 on 2022-08-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='post_images/default.jpg', null=True, upload_to='post_images/', verbose_name='Image'),
        ),
    ]
