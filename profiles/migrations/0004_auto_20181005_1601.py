# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profiles_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='description',
        ),
        migrations.AddField(
            model_name='profiles',
            name='email',
            field=models.CharField(default='my email default', max_length=40),
        ),
    ]
