# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-14 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('ApMaterno', models.CharField(max_length=50)),
                ('ApPaterno', models.CharField(max_length=50)),
                ('Telefono', models.PositiveIntegerField(blank=True, null=True)),
                ('Direccion', models.CharField(max_length=200)),
                ('FechaNacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Agricultor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.Persona')),
                ('CURP', models.CharField(max_length=18, null=True, unique=True)),
                ('RFC', models.CharField(max_length=18, null=True, unique=True)),
            ],
            bases=('usuario.persona',),
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='usuario.Persona')),
                ('Cargo', models.CharField(choices=[('GR', 'GERENTE'), ('AD', 'ADMINISTRADOR'), ('SP', 'SUPERVISOR')], max_length=2)),
            ],
            bases=('usuario.persona',),
        ),
    ]