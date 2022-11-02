# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-05 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_auto_20180401_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessaccountinfo',
            name='company_type',
            field=models.IntegerField(choices=[(0, '互联网'), (1, '金融'), (2, '能源'), (3, '基础建设'), (4, '交通'), (5, '通信')], default=0, help_text='公司类型', verbose_name='公司类型'),
        ),
        migrations.AddField(
            model_name='businessaccountinfo',
            name='password',
            field=models.CharField(blank=True, help_text='密码', max_length=20, null=True, verbose_name='密码'),
        ),
    ]
