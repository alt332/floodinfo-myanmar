# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0002_auto_20150803_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeed',
            name='state',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='newsfeed',
            name='township',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
