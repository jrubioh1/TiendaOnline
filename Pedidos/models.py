from django.db import models
from django.contrib.auth import get_user_model

from Tienda.models import Producto

User=get_user_model #para obtener el usuario logueado

class Pedidos(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return self.id # la id se genera auto por la base de datos
    
    
    @property
    def total():
          pass


    class Meta:
            db_table='pedidos'
            verbose_name='pedido'
            verbose_name_plural='pedidos'
            ordering=['id']

class LineaPedido(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    producto_id=models.ForeignKey(Producto, on_delete= models.CASCADE)


