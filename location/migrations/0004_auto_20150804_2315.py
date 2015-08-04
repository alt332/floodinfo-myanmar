# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20150804_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='district',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=9, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=12, decimal_places=9, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='status',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='township',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
