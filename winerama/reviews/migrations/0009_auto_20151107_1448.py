# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
