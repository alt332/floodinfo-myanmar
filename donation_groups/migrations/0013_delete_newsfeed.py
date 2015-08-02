# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donation_groups', '0012_auto_20150802_2136'),
    ]

    database_operations = [
        migrations.AlterModelTable('Newsfeed', 'newsfeed_newsfeed')
    ]

    state_operations = [
        migrations.DeleteModel('Newsfeed')
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations
        )
    ]
