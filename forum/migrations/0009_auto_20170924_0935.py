# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-24 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_lastmsg_msg_read'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]
