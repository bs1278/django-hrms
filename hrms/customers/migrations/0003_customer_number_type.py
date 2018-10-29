# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-29 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20181029_0546'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='number_type',
            field=models.CharField(blank=True, choices=[('Office', 'OFFICE'), ('Personal', 'PERSONAL')], max_length=25, null=True, verbose_name='Email Type'),
        ),
    ]
