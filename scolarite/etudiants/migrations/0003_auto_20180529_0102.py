# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-29 01:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiants', '0002_auto_20180528_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='domaine',
            field=models.CharField(choices=[('MI', 'MI')], default='MI', max_length=20),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='filiere',
            field=models.CharField(choices=[('I', 'Informatique')], default='I', max_length=20),
        ),
        migrations.AddField(
            model_name='etudiant',
            name='specialite',
            field=models.CharField(choices=[('SI', "Systeme d'information")], default='SI', max_length=20),
        ),
    ]
