# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0061_auto_20171129_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='calls',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Accounts'),
        ),
    ]
