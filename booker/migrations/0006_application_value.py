# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-22 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0005_remove_application_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='value',
            field=models.NullBooleanField(choices=[(None, 'Respond (Accept/Decline)'), (True, 'Accept'), (False, 'Decline')], default=None),
        ),
    ]
