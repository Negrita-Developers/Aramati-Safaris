# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 11:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0038_auto_20181107_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guaranteedsafaris',
            name='book_before',
        ),
        migrations.RemoveField(
            model_name='guaranteedsafaris',
            name='depature_date',
        ),
    ]
