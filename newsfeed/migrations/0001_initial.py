# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsfeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('show_hide', models.BooleanField(default=False, verbose_name=b'Hide')),
                ('description', models.TextField()),
                ('spam_report_count', models.IntegerField(default=0)),
                ('dam_condition', models.IntegerField(default=0, choices=[(0, b'Unknown'), (1, b'Normal'), (2, b'Bad'), (3, b'Very Bad')])),
                ('river_condition', models.IntegerField(default=0, choices=[(0, b'Unknown'), (1, b'Normal'), (2, b'Bad'), (3, b'Very Bad')])),
                ('posted_time', models.DateTimeField(default=django.utils.timezone.now, blank=True)),
            ],
        ),
    ]
