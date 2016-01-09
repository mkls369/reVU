# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0028_auto_20151226_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='name',
        ),
    ]
