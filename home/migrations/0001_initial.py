# Generated by Django 4.1.2 on 2022-11-15 12:35

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('kind', models.CharField(max_length=255)),
            ],
        ),
    ]
