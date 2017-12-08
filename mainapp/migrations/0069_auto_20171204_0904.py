# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0068_accounts_onboarded'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='ring_timeout',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='available_from',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='available_to',
            field=models.IntegerField(default=24),
        ),
    ]
