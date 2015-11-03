# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('indeed', '0007_querysearchhistory_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSearchHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('query', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='querysearchhistory',
            name='trade',
        ),
        migrations.RemoveField(
            model_name='searchhistory',
            name='trade',
        ),
        migrations.RemoveField(
            model_name='searchhistory',
            name='user',
        ),
        migrations.DeleteModel(
            name='QuerySearchHistory',
        ),
        migrations.DeleteModel(
            name='SearchHistory',
        ),
    ]
