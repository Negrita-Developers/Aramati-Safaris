# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 21:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0059_auto_20181108_0007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guaranteedsafaris',
            old_name='package',
            new_name='package',
        ),
    ]