# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 04:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_remove_contest_source'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contestproblem',
            options={'verbose_name': '比赛题目', 'verbose_name_plural': '比赛题目'},
        ),
    ]
