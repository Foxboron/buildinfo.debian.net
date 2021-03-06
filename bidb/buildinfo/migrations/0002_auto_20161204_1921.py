# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-04 19:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buildinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
            options={
                'ordering': ('name',),
                'get_latest_by': 'created',
            },
        ),
        migrations.AddField(
            model_name='buildinfo',
            name='build_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='buildinfo',
            name='environment',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildinfo',
            name='build_origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='buildinfo.Origin'),
        ),
    ]
