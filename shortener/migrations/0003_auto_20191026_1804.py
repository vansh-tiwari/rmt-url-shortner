# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-10-26 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_rmturl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rmturl',
            name='shortcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]