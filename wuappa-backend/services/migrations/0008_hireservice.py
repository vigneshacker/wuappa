# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 11:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0007_remove_category_cities'),
    ]

    operations = [
        migrations.CreateModel(
            name='HireService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=255)),
                ('comments', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PEN', 'Pending'), ('ACP', 'Accept'), ('CAN', 'Cancel'), ('REJ', 'Reject')], default='PEN', max_length=3)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL, verbose_name='Client')),
                ('professional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professional', to=settings.AUTH_USER_MODEL, verbose_name='Professional')),
                ('services', models.ManyToManyField(related_name='hire_services', to='services.Service')),
            ],
        ),
    ]
