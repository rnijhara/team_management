# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamapp', '0002_auto_20170615_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='teammemberrole',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
