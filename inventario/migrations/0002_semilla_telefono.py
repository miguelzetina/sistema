# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-14 19:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='semilla',
            name='Telefono',
            field=models.PositiveIntegerField(default=9341051950),
        ),
    ]