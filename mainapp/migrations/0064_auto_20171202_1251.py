# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-02 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0063_auto_20171202_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='best_time_to_contact',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
