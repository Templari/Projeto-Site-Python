# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0012_auto_20171021_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exames',
            name='icon',
            field=models.FileField(blank=True, upload_to='clinica/exames/icons'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='file',
            field=models.FileField(blank=True, upload_to='clinica/pacientes/exames'),
        ),
    ]
