# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-02-16 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewrMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interviwer_id', models.CharField(max_length=100, null=True)),
                ('interviwer_name', models.CharField(max_length=255, null=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('available_date', models.DateTimeField(null=True)),
                ('time_slot', models.CharField(max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchedulingMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_id', models.CharField(blank=True, max_length=100, null=True)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('job_code', models.CharField(blank=True, max_length=100, null=True)),
                ('apply_position', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('interview_date', models.DateTimeField(null=True)),
                ('time_slot', models.CharField(max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]