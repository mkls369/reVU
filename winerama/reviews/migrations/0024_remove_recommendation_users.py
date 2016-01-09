# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0023_auto_20151226_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='users',
        ),
    ]
