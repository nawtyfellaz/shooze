# Generated by Django 2.2 on 2020-06-12 14:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20200612_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='owner',
            field=models.OneToOneField(null=True, on_delete='marchant', related_name='marchant', to=settings.AUTH_USER_MODEL),
        ),
    ]