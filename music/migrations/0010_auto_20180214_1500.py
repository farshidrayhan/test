# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-14 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_drugs_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
