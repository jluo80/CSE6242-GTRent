# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-15 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtrent', '0013_auto_20160415_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yelp',
            name='IsWalk',
            field=models.BooleanField(default=True),
        ),
    ]
