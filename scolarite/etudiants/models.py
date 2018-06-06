# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


SPECIALITES = (
    ("Systeme d'information", "Systeme d'information"),
)
FILIERES = (
    ("Informatique", "Informatique"),
)
DOMAINES = (
    ("MI", "MI"),
)

PARCOURS = (
    ('L1', 'L1'),
    ('L2', 'L2'),
    ('L3', 'L3'),
    ('M1', 'M1'),
    ('M2', 'M2'),
)

class Module(models.Model):
    label = models.CharField(max_length=30)
    coef = models.IntegerField()
    unite = models.CharField(max_length=30)
    parcours = models.CharField(
        max_length=2, default=PARCOURS[0][0], choices=PARCOURS)

    def __str__(self):
        return self.label

class Moyenne(models.Model):
    value = models.FloatField()
    module = models.ForeignKey(Module)

    def __str__(self):
        return '{0} {1}'.format(self.value, self.module)

class Etudiant(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    date_naiss = models.DateField()
    num = models.IntegerField()
    specialite = models.CharField(
        max_length=21, default=SPECIALITES[0][0], choices=SPECIALITES)
    filiere = models.CharField(
        max_length=20, default=FILIERES[0][0], choices=FILIERES)
    domaine = models.CharField(
        max_length=20, default=DOMAINES[0][0], choices=DOMAINES)
    parcours = models.CharField(
        max_length=2, default=PARCOURS[0][0], choices=PARCOURS)

    moyennes = models.ManyToManyField(Moyenne)

    def __str__(self):
        return self.nom
    
    def calcule_moy_generale(self):
        sum = 0
        totalcoef = 0
        for m in self.moyennes.all():
            sum+=(m.value)*m.module.coef
            totalcoef+= m.module.coef
        return sum/float(totalcoef)