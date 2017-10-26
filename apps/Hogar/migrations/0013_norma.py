# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 23:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hogar', '0012_auto_20171026_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Norma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15, unique=True)),
                ('estandar', models.CharField(max_length=150)),
                ('fundamento', models.TextField(max_length=800)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hogar.Medida')),
            ],
            options={
                'verbose_name': 'Norma',
                'verbose_name_plural': 'Normas',
            },
        ),
    ]
