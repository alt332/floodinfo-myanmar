# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_groups', '0013_delete_newsfeed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationgroup',
            name='description',
            field=models.TextField(),
        ),
    ]
