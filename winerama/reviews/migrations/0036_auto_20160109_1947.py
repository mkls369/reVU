# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0035_auto_20151230_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendation',
            old_name='Subjects',
            new_name='subjects',
        ),
    ]
