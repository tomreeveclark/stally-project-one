# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stally', '0014_auto_20160313_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='stall',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]