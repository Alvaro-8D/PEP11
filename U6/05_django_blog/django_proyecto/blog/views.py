#blog/views.py
from .models import Post
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView, 
                                  DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect

class VistaListaPosts(ListView):
    model = Post
    template_name = "home.html"

class VistaDetallePost(DetailView):
    model = Post
    template_name = "detalle_post.html"

class VistaCrearPost(LoginRequiredMixin, CreateView): 
    model = Post
    template_name = "nuevo_post.html"
    fields = ["titulo", "cuerpo"] # Campos del modelo Post que se mostrarán en el formulario
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class VistaActualizarPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView): # nuevo
    model = Post
    template_name = "actualizar_post.html"
    fields = ["titulo", "cuerpo"]

    def test_func(self):
        return (self.get_object().autor == self.request.user) or (self.request.user.is_staff)
    
    def handle_no_permission(self): 
        messages.error(self.request, "NO tienes permiso para ACTUALIZAR este post D:<")
        return redirect("detalle_post", pk=self.get_object().pk)


class VistaEliminarPost(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # nuevo
    model = Post
    template_name = "eliminar_post.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return (self.get_object().autor == self.request.user) or (self.request.user.is_staff)

    def handle_no_permission(self): 
        messages.error(self.request, "NO tienes permiso para BORRAR este post D:<")
        return redirect("detalle_post", pk=self.get_object().pk)
