# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_wine_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='likes',
        ),
    ]
