# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_groups', '0003_remove_donationgroup_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donationgroup',
            old_name='facebookurl',
            new_name='facebook_url',
        ),
    ]
