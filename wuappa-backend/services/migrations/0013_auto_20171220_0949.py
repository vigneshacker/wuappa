# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0012_hireservice_charges'),
    ]

    operations = [
        migrations.AddField(
            model_name='hireservice',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='hireservice',
            name='notified_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
