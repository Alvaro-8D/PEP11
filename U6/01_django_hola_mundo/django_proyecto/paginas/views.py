# pages/views.py
from django.shortcuts import render
from django.http import HttpResponse

def vista_pagina_inicio(request):
    return HttpResponse("Hola mundo, me llamo Álvaro!")