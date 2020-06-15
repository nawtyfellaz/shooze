# Generated by Django 2.2 on 2020-06-15 05:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_delete_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='category',
            name='object_id',
        ),
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='category',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]