# Generated by Django 3.2.5 on 2021-08-24 20:57

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='LangTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='ساخت')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='آپدیت')),
                ('status', models.CharField(choices=[('draft', 'در حال انتظار'), ('published', 'منتشر شده')], default='draft', max_length=60, verbose_name='وضعیت')),
                ('title', models.CharField(max_length=25)),
                ('name', models.CharField(max_length=25)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('url', models.URLField(max_length=100)),
                ('stars', models.IntegerField(default=0)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True)),
                ('summary', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('video', models.URLField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.category')),
                ('langtag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.langtag')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
