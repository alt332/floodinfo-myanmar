# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_auto_20150804_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
