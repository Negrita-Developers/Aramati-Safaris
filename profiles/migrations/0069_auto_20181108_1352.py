# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0068_joinedsafaris'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price1', models.IntegerField(default=0)),
                ('price2', models.IntegerField(default=0)),
                ('price3', models.IntegerField(default=0)),
                ('price4', models.IntegerField(default=0)),
                ('price5', models.IntegerField(default=0)),
                ('price6', models.IntegerField(default=0)),
                ('price7', models.IntegerField(default=0)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Packages')),
            ],
        ),
        migrations.CreateModel(
            name='PeakSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price1', models.IntegerField(default=0)),
                ('price2', models.IntegerField(default=0)),
                ('price3', models.IntegerField(default=0)),
                ('price4', models.IntegerField(default=0)),
                ('price5', models.IntegerField(default=0)),
                ('price6', models.IntegerField(default=0)),
                ('price7', models.IntegerField(default=0)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Packages')),
            ],
        ),
        migrations.AddField(
            model_name='joinedsafaris',
            name='Location',
            field=models.CharField(default='location', max_length=15),
        ),
    ]