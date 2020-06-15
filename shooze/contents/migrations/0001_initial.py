# Generated by Django 2.2 on 2020-06-14 14:39

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import shooze.contents.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(blank=True, max_length=120, null=True, unique=True, verbose_name='category_title')),
                ('slug', models.SlugField(blank=True, max_length=350, null=True, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('object_id', models.PositiveIntegerField()),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categroies',
                'ordering': ['title', '-created', '-modified'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('object_id', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=shooze.contents.models.image_file_path, verbose_name='upload_images')),
            ],
            options={
                'verbose_name': 'Content File',
                'verbose_name_plural': 'Content Files',
                'ordering': ['-created'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('active', models.BooleanField(default=True)),
                ('object_id', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]