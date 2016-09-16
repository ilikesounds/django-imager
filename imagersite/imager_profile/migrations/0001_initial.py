# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 00:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagerProfile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('imager_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='address', serialize=False, to='imager_profile.ImagerProfile')),
                ('street_addr', models.CharField(blank=True, max_length=128, verbose_name='Street Address')),
                ('unit', models.CharField(blank=True, max_length=8, verbose_name='Unit')),
                ('city', models.CharField(blank=True, max_length=64, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=4, verbose_name='state')),
                ('post_code', models.CharField(blank=True, max_length=5, verbose_name='Postal Code')),
            ],
        ),
        migrations.CreateModel(
            name='CameraType',
            fields=[
                ('imager_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='camera_type', serialize=False, to='imager_profile.ImagerProfile')),
                ('camera_type', models.CharField(blank=True, max_length=64, verbose_name='Camera Type')),
            ],
        ),
        migrations.CreateModel(
            name='PhotographyType',
            fields=[
                ('imager_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='photography_type', serialize=False, to='imager_profile.ImagerProfile')),
                ('photography_type', models.CharField(choices=[('Nature', 'Nature'), ('Portrait', 'Portrait'), ('Family', 'Family'), ('Urban', 'Urban'), ('Astronomy', 'Astronomy')], max_length=32, verbose_name='Photography Type')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('imager_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='social', serialize=False, to='imager_profile.ImagerProfile')),
                ('social_type', models.CharField(blank=True, max_length=64, verbose_name='Social Medial Type')),
                ('social_url', models.CharField(blank=True, max_length=64, verbose_name='Social Media URL')),
            ],
        ),
        migrations.AddField(
            model_name='imagerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]