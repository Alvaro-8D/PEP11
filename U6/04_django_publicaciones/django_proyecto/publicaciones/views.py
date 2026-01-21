# publicaciones/views.py
from django.shortcuts import render
from .models import Publicacion

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, "lista_publicaciones.html", {"publicaciones":publicaciones})
