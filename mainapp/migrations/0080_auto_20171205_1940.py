# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 19:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0079_auto_20171205_1858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='usagemeter_minutes',
            new_name='usagemeter_seconds',
        ),
        migrations.AlterField(
            model_name='accounts',
            name='accountstatus',
            field=models.CharField(default='active', max_length=50),
        ),
    ]
