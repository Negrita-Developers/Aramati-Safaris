# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0043_auto_20181107_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joingroup',
            name='title',
            field=models.CharField(default='title', max_length=120),
        ),
    ]
