# Generated by Django 4.1 on 2022-08-15 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_alter_postcomment_options_alter_postcomment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.postcomment', verbose_name='Parent comment'),
        ),
    ]
