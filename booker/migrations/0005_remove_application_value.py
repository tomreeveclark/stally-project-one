# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-22 07:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0004_auto_20160321_0938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='value',
        ),
    ]