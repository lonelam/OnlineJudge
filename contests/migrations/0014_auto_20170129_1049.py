# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 02:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0013_auto_20170127_1517'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contestsubmission',
            options={'ordering': ('submission', 'problem'), 'verbose_name': '比赛提交', 'verbose_name_plural': '比赛提交'},
        ),
        migrations.AddField(
            model_name='contestaccount',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='注册时间'),
            preserve_default=False,
        ),
    ]