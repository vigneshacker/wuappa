# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-28 12:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0002_auto_20171227_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupon',
            old_name='costumer',
            new_name='user',
        ),
    ]