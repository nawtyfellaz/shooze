# Generated by Django 2.2 on 2020-06-12 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='terms',
            field=models.BooleanField(default=False),
        ),
    ]
