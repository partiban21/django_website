# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-10 03:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20171210_0325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
