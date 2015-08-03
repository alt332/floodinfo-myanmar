# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_groups', '0004_auto_20150731_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donationgroup',
            name='email',
        ),
        migrations.AlterField(
            model_name='phonenumber',
            name='donation_group',
            field=models.ForeignKey(related_name='phone_numbers', to='donation_groups.DonationGroup'),
        ),
    ]
