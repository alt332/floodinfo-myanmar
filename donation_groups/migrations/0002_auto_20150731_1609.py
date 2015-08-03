# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationgroup',
            name='donation_location',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='donationgroup',
            name='facebookurl',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='donationgroup',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
