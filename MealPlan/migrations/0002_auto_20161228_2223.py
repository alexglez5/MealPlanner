# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MealPlan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.CharField(max_length=200),
        ),
    ]
