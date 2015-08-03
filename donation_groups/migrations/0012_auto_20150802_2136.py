# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('donation_groups', '0011_auto_20150802_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeed',
            name='posted_time',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True),
        ),
    ]
