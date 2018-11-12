# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 21:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0056_auto_20181107_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guaranteedsafaris',
            name='Enter_Safari_Package',
        ),
        migrations.AddField(
            model_name='guaranteedsafaris',
            name='package',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.Packages'),
        ),
        migrations.AlterField(
            model_name='lowseason',
            name='package',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.Packages'),
        ),
        migrations.AlterField(
            model_name='packages',
            name='name',
            field=models.CharField(default='package', max_length=30),
        ),
    ]