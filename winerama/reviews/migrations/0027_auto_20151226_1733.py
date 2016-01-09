# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0026_auto_20151226_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='users',
            field=models.ForeignKey(default=25, to=settings.AUTH_USER_MODEL),
        ),
    ]
