# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0078_joinedsafaris_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='highseason',
            name='SRS',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='joinedsafaris',
            name='Hotel_Star',
            field=models.CharField(choices=[('2 star', '2 star'), ('3 star', '3 star'), ('4 star', '4 star'), ('Treetops Aberdare', 'Treetops Aberdare'), ('Ark Aberdare', 'Ark Aberdare')], default='hotelstar', max_length=20),
        ),
        migrations.AddField(
            model_name='lowseason',
            name='SRS',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='peakseason',
            name='SRS',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
