# Generated by Django 4.1 on 2022-08-20 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0014_alter_seo_keywords_connection'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=25, verbose_name="Visitor's Ip Address ")),
                ('authenticated_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ')),
            ],
            options={
                'verbose_name': 'Logged ip',
                'verbose_name_plural': "Logged ip's",
            },
        ),
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visits_count', models.IntegerField(default=0, verbose_name='Count of Visitors')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.iplog', verbose_name='Visitor ')),
            ],
            options={
                'verbose_name': 'Visitor',
                'verbose_name_plural': 'Visitors',
            },
        ),
    ]
