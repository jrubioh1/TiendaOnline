from django.db import models
from django.contrib.auth import get_user_model

from Tienda.models import Producto
from django.db.models import F, Sum, FloatField

User=get_user_model() #para obtener el usuario logueado

class Pedidos(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return self.id # la id se genera auto por la base de datos
    
    
    @property
    def total():
          return self.lineapedido_set.aggregate(
                
            total=Sum(F('precio')*F('cantidad'), output_fiel=FloatField())


          )['total']


    class Meta:
            db_table='pedidos'
            verbose_name='pedido'
            verbose_name_plural='pedidos'
            ordering=['id']

class LineaPedido(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    producto_id=models.ForeignKey(Producto, on_delete= models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
          
          return f'{self.catidad} unidades de {self.producto_id.nombre}'
    class Meta:
            db_table='lineapedidos'
            verbose_name='Línea Pedido'
            verbose_name_plural='Líneas Pedidos'
            ordering=['id']


