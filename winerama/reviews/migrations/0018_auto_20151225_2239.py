# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0017_recommendations'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recommendations',
            new_name='Recommendation',
        ),
    ]
