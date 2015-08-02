# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('donation_groups', '0010_auto_20150801_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeed',
            name='posted_time',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AlterField(
            model_name='newsfeed',
            name='dam_condition',
            field=models.IntegerField(default=0, choices=[(0, b'Unknown'), (1, b'Normal'), (2, b'Bad'), (3, b'Very Bad')]),
        ),
        migrations.AlterField(
            model_name='newsfeed',
            name='river_condition',
            field=models.IntegerField(default=0, choices=[(0, b'Unknown'), (1, b'Normal'), (2, b'Bad'), (3, b'Very Bad')]),
        ),
    ]
