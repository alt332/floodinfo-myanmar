# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_groups', '0009_auto_20150801_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeed',
            name='dam_condition',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='newsfeed',
            name='river_condition',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='newsfeed',
            name='show_hide',
            field=models.BooleanField(default=False, verbose_name=b'Hide'),
        ),
    ]
