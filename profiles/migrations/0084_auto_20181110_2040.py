# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-10 17:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0083_auto_20181110_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinedsafaris',
            name='book_before',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='joinedsafaris',
            name='depature_date',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]
