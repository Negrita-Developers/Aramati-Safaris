# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 11:35
from __future__ import unicode_literals

from django.db import migrations, models

import datetime as date
from datetime import datetime; datetime.now()


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0035_remove_joingroup_bookbefore'),
    ]

    operations = [
        migrations.AddField(
            model_name='guaranteedsafaris',
            name='book_before',
            field=models.DateField(default=datetime.now()),
        ),
        migrations.AddField(
            model_name='guaranteedsafaris',
            name='depature_date',
            field=models.DateField(default=datetime.now()),
        ),
        migrations.AlterField(
            model_name='packages',
            name='name',
            field=models.CharField(default='packagename', max_length=30),
        ),
    ]