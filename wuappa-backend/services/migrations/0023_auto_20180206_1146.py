# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-06 11:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0022_hireservicerefuse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hireservice',
            name='services',
        )
    ]
