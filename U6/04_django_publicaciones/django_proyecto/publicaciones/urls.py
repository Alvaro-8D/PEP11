# publicaciones/urls.py
from django.urls import path
# from .views import lista_publicaciones
from .views import ListaPublicaciones # nuevo

# urlpatterns = [
#     path("", lista_publicaciones, name="home"),
# ]

urlpatterns = [
    path("", ListaPublicaciones.as_view(), name="home"),
]





