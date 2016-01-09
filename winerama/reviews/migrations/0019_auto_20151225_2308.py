# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0018_auto_20151225_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='name',
        ),
        migrations.AddField(
            model_name='recommendation',
            name='wines',
            field=models.ManyToManyField(to='reviews.Wine'),
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='users',
        ),
        migrations.AddField(
            model_name='recommendation',
            name='users',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
