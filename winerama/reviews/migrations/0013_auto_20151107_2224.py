# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_auto_20151107_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='user_name',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
