# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20170519_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='drug_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug_id', models.CharField(max_length=50)),
                ('fingerprint', models.CharField(max_length=900)),
            ],
        ),
    ]
