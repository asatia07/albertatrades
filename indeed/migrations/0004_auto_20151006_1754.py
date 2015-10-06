# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('indeed', '0003_auto_20151003_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuerySearchHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('trade', models.ForeignKey(to='indeed.Trade')),
            ],
        ),
        migrations.AlterField(
            model_name='searchhistory',
            name='user',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
