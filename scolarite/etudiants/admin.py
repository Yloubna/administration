# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Etudiant, Moyenne, Module

# Register your models here.
admin.site.register(Etudiant)
admin.site.register(Module)
admin.site.register(Moyenne)