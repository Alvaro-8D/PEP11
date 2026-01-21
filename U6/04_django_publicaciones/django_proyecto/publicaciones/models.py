# foro/models.py
from django.db import models

class Publicacion(models.Model):
    texto = models.TextField()
    
    def __str__(self): # nuevo
        return self.texto[:50]