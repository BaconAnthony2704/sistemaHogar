# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-25 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Hogar', '0002_delete_prevencion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prevencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(max_length=600)),
            ],
            options={
                'verbose_name': 'Prevencion',
                'verbose_name_plural': 'Prevenciones',
            },
        ),
    ]
