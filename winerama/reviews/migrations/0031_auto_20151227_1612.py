# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0030_recommendation_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='users',
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='wines',
        ),
        migrations.DeleteModel(
            name='Recommendation',
        ),
    ]
