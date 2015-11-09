# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_remove_star_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='star',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='star',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
