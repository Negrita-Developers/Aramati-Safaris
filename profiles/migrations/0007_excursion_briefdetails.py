# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20181016_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursion',
            name='briefdetails',
            field=models.SlugField(default='my details'),
        ),
    ]