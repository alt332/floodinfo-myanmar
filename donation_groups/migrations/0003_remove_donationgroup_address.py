# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_groups', '0002_auto_20150731_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donationgroup',
            name='address',
        ),
    ]
