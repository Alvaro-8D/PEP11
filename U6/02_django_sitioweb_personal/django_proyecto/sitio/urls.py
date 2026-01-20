# sitio/urls.py
from django.urls import path
from .views import vista_pagina_inicio , vista_acercade # nuevo

urlpatterns = [
    path("about/", vista_acercade), # nuevo
    path("",vista_pagina_inicio),
]