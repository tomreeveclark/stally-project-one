# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stally', '0013_auto_20160313_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='follows',
            field=models.ManyToManyField(related_name='followedby', to='stally.Market'),
        ),
    ]