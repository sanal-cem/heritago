# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-01 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heritages', '0003_auto_20170501_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='username'),
        ),
    ]
