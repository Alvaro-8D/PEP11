# sitio/views.py
from django.http import HttpResponse
from django.shortcuts import render

def vista_pagina_inicio(request):
    return HttpResponse("Inicio")

def vista_acercade(request):
    context = {
        "nombre": "Ana",
        "edad": 44, #
    }
    return render(request, "sitio/about.html", context)