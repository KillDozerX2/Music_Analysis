# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-28 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Album', models.CharField(max_length=200)),
                ('Artist', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=50)),
                ('IntroDetails', models.TextField(null=True)),
                ('Verse1Details', models.TextField(null=True)),
                ('Verse2Details', models.TextField(null=True)),
                ('OutroDetails', models.TextField(null=True)),
                ('Image_src', models.FileField(upload_to=b'')),
            ],
        ),
    ]
