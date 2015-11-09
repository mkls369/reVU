# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
