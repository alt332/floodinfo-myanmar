# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_groups', '0007_news'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News',
            new_name='Newsfeed',
        ),
    ]
