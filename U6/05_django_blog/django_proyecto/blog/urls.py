# blog/urls.py
from django.urls import path
from .views import detalle_post, lista_posts # nuevo

urlpatterns = [
    path("post/<int:pk>/", detalle_post, name="detalle_post"), # new
    path("", lista_posts, name="home"),
]