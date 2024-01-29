from django.contrib import admin

from Pedidos.models import LineaPedido,Pedidos

admin.site.register(Pedidos,LineaPedido)
