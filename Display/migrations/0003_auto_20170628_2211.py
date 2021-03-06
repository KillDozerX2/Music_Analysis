# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-28 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Display', '0002_auto_20170628_2201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='BIO',
            new_name='Bio',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='Name',
            new_name='Title',
        ),
        migrations.AlterField(
            model_name='genre',
            name='Logo',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
