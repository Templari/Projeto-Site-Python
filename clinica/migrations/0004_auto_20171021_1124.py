# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 13:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0003_auto_20171021_1047'),
    ]

    operations = [
        migrations.CreateModel(
            name='InserirExame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to='media/pacientes/exames')),
            ],
        ),
        migrations.AlterModelOptions(
            name='paciente',
            options={'ordering': ['criado_em'], 'verbose_name': 'nome', 'verbose_name_plural': 'Pacientes'},
        ),
        migrations.AddField(
            model_name='inserirexame',
            name='nome',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.Paciente'),
        ),
    ]
