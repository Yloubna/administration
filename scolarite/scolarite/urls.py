"""scolarite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from etudiants.views import liste, liste_with_filter, diplome, attestation, delete, create, update

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="acceuil.html"), name="acceuil"),
    url(r'^liste/$', liste, name="liste"),
    url(r'^liste/create/$', create, name='create'),
    url(r'^liste/(?P<pk>\d+)/update/$', update, name='update'),
    url(r'^liste/(?P<parcours>\w+)/$', liste_with_filter, name="liste"),
    url(r'^diplome/(?P<id>[0-9]+)/$', diplome, name="diplome"),
    url(r'^attestation/(?P<id>[0-9]+)/$', attestation, name="attestation"),
    url(r'^delete/(?P<id>[0-9]+)/$', delete, name='delete'),
]
