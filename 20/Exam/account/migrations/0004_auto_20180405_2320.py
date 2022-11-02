# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-05 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import utils.basemodels


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20180404_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='resume',
            field=models.FileField(blank=True, help_text='resume/简历', null=True, upload_to=utils.basemodels.ModelHelper.upload_path, verbose_name='简历'),
        ),
    ]
