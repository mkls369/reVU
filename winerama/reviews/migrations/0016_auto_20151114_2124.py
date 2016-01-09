# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0015_auto_20151109_2224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='star',
            name='wine',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Star',
        ),
    ]
