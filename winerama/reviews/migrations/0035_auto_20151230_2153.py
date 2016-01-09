# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0034_auto_20151227_1927'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wine',
            new_name='Subject',
        ),
        migrations.RemoveField(
            model_name='cluster',
            name='users',
        ),
        migrations.RemoveField(
            model_name='review',
            name='wine',
        ),
        migrations.RemoveField(
            model_name='recommendation',
            name='wines',
        ),
        migrations.AddField(
            model_name='recommendation',
            name='Subjects',
            field=models.ManyToManyField(to='reviews.Subject'),
        ),
        migrations.DeleteModel(
            name='Cluster',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
