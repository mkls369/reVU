# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0029_remove_recommendation_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
