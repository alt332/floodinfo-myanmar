# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_groups', '0008_auto_20150731_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsfeed',
            name='show_hide',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsfeed',
            name='spam_report_count',
            field=models.IntegerField(default=0),
        ),
    ]
