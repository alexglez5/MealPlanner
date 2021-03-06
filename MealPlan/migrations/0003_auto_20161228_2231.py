# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MealPlan', '0002_auto_20161228_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='GI',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='food',
            name='carbs',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='food',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='fat',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='food',
            name='protein',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]
