# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0073_auto_20181108_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinedsafaris',
            name='Enter_Safari_Package',
        ),
        migrations.AddField(
            model_name='joinedsafaris',
            name='package',
            field=models.ForeignKey( on_delete=django.db.models.deletion.CASCADE, to='profiles.Packages'),
        ),
    ]