# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 11:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0037_auto_20181107_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guaranteedsafaris',
            name='book_before',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='guaranteedsafaris',
            name='depature_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
