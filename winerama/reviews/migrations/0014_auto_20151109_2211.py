# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_auto_20151107_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='user_name',
            field=models.CharField(max_length=100),
        ),
    ]
