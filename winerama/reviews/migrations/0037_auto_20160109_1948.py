# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0036_auto_20160109_1947'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendation',
            old_name='subjects',
            new_name='Subjects',
        ),
    ]
