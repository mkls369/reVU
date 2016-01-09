# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0033_auto_20151227_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='user',
            field=models.ForeignKey(related_query_name=b'recs', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
