# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-06-24 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_auto_20190624_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='new_username',
        ),
    ]