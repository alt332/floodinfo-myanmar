# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('district', models.CharField(max_length=255)),
                ('township', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(max_digits=12, decimal_places=9)),
                ('longitude', models.DecimalField(max_digits=12, decimal_places=9)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
    ]
