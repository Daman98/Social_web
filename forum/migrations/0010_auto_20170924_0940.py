# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20170924_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='text',
            field=models.CharField(max_length=1000),
        ),
    ]
