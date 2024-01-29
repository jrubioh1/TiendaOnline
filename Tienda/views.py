from django.shortcuts import render
from Tienda.models import Producto, CategoriaProd


def tienda(request):
  productos=Producto.objects.all()
  return render(request, 'Tienda/tienda.html',{"productos": productos})