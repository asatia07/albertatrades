# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indeed', '0006_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='querysearchhistory',
            name='location',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
