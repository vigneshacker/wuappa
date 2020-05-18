# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-06 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0023_auto_20180206_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='HireServiceService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hireservice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.HireService')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
            ],
        ),
        migrations.AddField(
            model_name='hireservice',
            name='services',
            field=models.ManyToManyField(related_name='hirings', through='services.HireServiceService', to='services.Service'),
        ),
    ]
