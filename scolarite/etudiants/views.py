# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import Etudiant
from .forms import EtudiantForm

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
    return render(request, 'liste.html', context)       

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


def delete(request,id):
    etudiant = Etudiant.objects.get(id=id)
    etudiant.delete()
    return render(request,'liste.html')

def save_etudiant_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            etudiants = Etudiant.objects.all()
            data['html_etudiant_list'] = render_to_string('liste.html', {
                'etudiants': etudiants
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def create(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
    else:
        form = EtudiantForm()
    return save_etudiant_form(request, form, 'create.html')


def update(request, pk):
    etudiant = get_object_or_404(Etudiant, pk=pk)
    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=etudiant)
    else:
        form = EtudiantForm(instance=etudiant)
    return save_etudiant_form(request, form, 'update.html')