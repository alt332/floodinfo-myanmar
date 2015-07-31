# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_groups', '0005_auto_20150731_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phonenumber',
            name='donation_group',
        ),
        migrations.AddField(
            model_name='donationgroup',
            name='phone_numbers',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='PhoneNumber',
        ),
    ]
