# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0010_add_related_name_to_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='date_uploaded',
        ),
        migrations.AlterField(
            model_name='album',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date Created'),
        ),
    ]
