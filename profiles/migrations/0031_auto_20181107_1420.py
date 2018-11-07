      # -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-07 11:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import datetime as date
from datetime import datetime; datetime.now()

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0030_auto_20181107_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='LowSeason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price1', models.IntegerField(default=0)),
                ('price2', models.IntegerField(default=0)),
                ('price3', models.IntegerField(default=0)),
                ('price4', models.IntegerField(default=0)),
                ('price5', models.IntegerField(default=0)),
                ('price6', models.IntegerField(default=0)),
                ('price7', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='package name', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='guaranteedsafaris',
            name='Enter_Hotel_Star',
        ),
        migrations.RemoveField(
            model_name='guaranteedsafaris',
            name='price1',
        ),
        migrations.RemoveField(
            model_name='guaranteedsafaris',
            name='price2',
        ),
        migrations.RemoveField(
            model_name='guaranteedsafaris',
            name='price3',
        ),
        migrations.RemoveField(
            model_name='guaranteedsafaris',
            name='price4',
        ),
        migrations.RemoveField(
            model_name='guaranteedsafaris',
            name='price5',
        ),
        migrations.RemoveField(
            model_name='guaranteedsafaris',
            name='price6',
        ),
        migrations.RemoveField(
            model_name='guaranteedsafaris',
            name='price7',
        ),
        migrations.AddField(
            model_name='guaranteedsafaris',
            name='Accomodation',
            field=models.CharField(choices=[('bg', 'Budget'), ('lx', 'Luxury')], default='accomodation', max_length=20),
        ),
        migrations.AddField(
            model_name='guaranteedsafaris',
            name='depature_date',
            field=models.DateField(default=datetime.now()),
        ),
        migrations.AlterField(
            model_name='guaranteedsafaris',
            name='book_before',
            field=models.DateField(default=datetime.now()),
        ),
        migrations.AddField(
            model_name='lowseason',
            name='package',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.Packages'),
        ),
    ]
