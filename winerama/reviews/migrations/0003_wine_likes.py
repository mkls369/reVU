# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_cluster'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
