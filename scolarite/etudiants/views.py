# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from .forms import EtudiantForm
from .models import Etudiant


# Create your views here.


def liste(request):
    etudiants = Etudiant.objects.all()
    context = {
        'etudiants': etudiants
    }
    return render(request, 'liste.html', context)

def liste_with_filter(request, parcours):
    etudiants = Etudiant.objects.filter(parcours=parcours)
    context = {
        'etudiants': etudiants
    }
    return render(request, 'listefiltred.html', context)
  
    


def diplome(request, id):
    etudiant = Etudiant.objects.get(id=id)
    context = {
        'etudiant': etudiant
    }
    return render(request, 'diplome.html', context)


def attestation(request, id):
    etudiant = Etudiant.objects.get(id=id)
    context = {
        'etudiant': etudiant
    }
    return render(request, 'attestation.html', context)


def delete(request, id):
    etudiant = Etudiant.objects.get(id=id)
    etudiant.delete()
    return render(request, 'liste.html')

class EtudiantUpdate(UpdateView):
    model = Etudiant
    form_class = EtudiantForm
    template_name = 'update_etudiant.html'

    def get_success_url(self):
        return reverse_lazy('liste')


def releve_de_notes(request, id):
    etudiant = get_object_or_404(Etudiant, pk=id)
    context = {
        'etudiant': etudiant
    }
    return render(request=request, template_name='releve.html', context=context)

def pv_deliberation(request):
    etudiants = Etudiant.objects.all()
    context = {
        'etudiants': etudiants
    }
    return render(request, 'pv.html', context)

