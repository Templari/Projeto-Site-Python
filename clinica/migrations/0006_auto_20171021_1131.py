# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0005_paciente_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='file',
            field=models.FileField(blank=True, upload_to='', verbose_name='clinica.InserirExame.file'),
        ),
    ]
