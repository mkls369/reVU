# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0020_auto_20151225_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='wines',
            field=models.ManyToManyField(to='reviews.Wine'),
        ),
    ]
