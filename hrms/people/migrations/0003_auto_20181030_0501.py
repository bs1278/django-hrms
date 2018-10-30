# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20181030_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empskillprofile',
            name='languages',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Language Skills'),
        ),
        migrations.AlterField(
            model_name='empskillprofile',
            name='management_skills',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Management Skills'),
        ),
        migrations.AlterField(
            model_name='empskillprofile',
            name='primary_skills',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Primary Skills'),
        ),
        migrations.AlterField(
            model_name='empskillprofile',
            name='secondary_skills',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Secondary Skills'),
        ),
    ]
