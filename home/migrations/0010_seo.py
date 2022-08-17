# Generated by Django 4.1 on 2022-08-17 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_socialmediaaccounts_account_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=50, verbose_name='Keywords Meta Tag')),
                ('description', models.TextField(verbose_name='Description Meta Tag')),
                ('isMain', models.BooleanField(verbose_name='Main Meta Tags for Site')),
            ],
            options={
                'verbose_name': 'Meta tag',
                'verbose_name_plural': 'Seo Meta tags',
            },
        ),
    ]