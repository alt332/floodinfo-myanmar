# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='type',
            new_name='state',
        ),
        migrations.AddField(
            model_name='location',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='rural_total_female',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='rural_total_male',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='status',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='total_female',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='total_male',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='urban_total_female',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='urban_total_male',
            field=models.IntegerField(default=0),
        ),
    ]
