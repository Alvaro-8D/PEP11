# empresa/urls.py
from django.urls import path
from .views import vista_pagina_inicio , VistaAcercaDe # nuevo

urlpatterns = [
    path("about/", VistaAcercaDe.as_view(), name="about"), # nuevo
    path("",vista_pagina_inicio, name="inicio"),
]

