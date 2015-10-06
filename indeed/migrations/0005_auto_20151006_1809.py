# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indeed', '0004_auto_20151006_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='querysearchhistory',
            old_name='user',
            new_name='user_id',
        ),
    ]
