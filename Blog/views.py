from django.shortcuts import render
from Blog.models import Categoria, Post



def blog(request):

    post= Post.objects.all()



    return render(request, 'Blog/blog.html', {"post": post})

def categoria(request, categoria_id):

    categoria= Categoria.objects.get(id=categoria_id)
    post= Post.objects.filter(categorias=categoria)
    return render(request, 'Blog/categoria.html',{'categoria': categoria, 'post': post})

