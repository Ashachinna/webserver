# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-14 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20160914_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Django_Subject_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=256, null=True)),
                ('content', models.CharField(blank=True, max_length=1024, null=True)),
            ],
        ),
    ]