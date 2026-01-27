#blog/views.py
from django.shortcuts import get_object_or_404, render # nuevo
from .models import Post

def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def detalle_post(request, pk): # new
    post = get_object_or_404(Post, pk=pk)
    return render(request, "detalle_post.html", {"post": post})