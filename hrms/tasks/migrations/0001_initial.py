# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-30 08:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('priority', models.CharField(blank=True, max_length=6, null=True, verbose_name='Priority')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created At')),
                ('due_date', models.DateField(blank=True, null=True, verbose_name='Due Date')),
                ('current_status', models.CharField(blank=True, max_length=10, null=True, verbose_name='Current Status')),
                ('result_status', models.CharField(blank=True, max_length=10, null=True, verbose_name='Result Status')),
            ],
            options={
                'verbose_name': 'Base Tasks',
                'verbose_name_plural': 'Base Tasks',
                'db_table': 'base_task',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='TaskAttachmentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(blank=True, help_text='attach any refference file for task', null=True, upload_to='tasks/', verbose_name='Attachement File')),
            ],
            options={
                'verbose_name': 'Task Attachement File',
            },
        ),
        migrations.CreateModel(
            name='DevelopmentTask',
            fields=[
                ('basetask_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tasks.BaseTask')),
                ('send_copy_email', models.BooleanField(default=True)),
                ('instructions', models.TextField(blank=True, help_text='Instructions/guidelines for task', null=True, verbose_name='Instructions')),
                ('attachment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.TaskAttachmentFile', verbose_name='Attchement')),
                ('employees', models.ManyToManyField(related_name='emplooyes', to='people.Employee', verbose_name='Employees')),
                ('review_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to='people.Employee', verbose_name='Review By')),
            ],
            options={
                'verbose_name': 'Development Task',
                'verbose_name_plural': 'Development Tasks',
            },
            bases=('tasks.basetask',),
        ),
        migrations.CreateModel(
            name='OperationTask',
            fields=[
                ('basetask_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tasks.BaseTask')),
                ('send_copy_email', models.BooleanField(default=True)),
                ('instructions', models.TextField(blank=True, null=True, verbose_name='Instructions')),
                ('attachment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.TaskAttachmentFile', verbose_name='Attchement')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Employee', verbose_name='Employee')),
            ],
            options={
                'verbose_name': 'Operation Task',
                'verbose_name_plural': 'Operation Tasks',
            },
            bases=('tasks.basetask',),
        ),
    ]
