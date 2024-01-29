from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre= models.CharField(max_length=50)
    created= models.DateTimeField(auto_now_add=True)# para que se inicie con la fecha en el que se crea de forma automatica
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:

        #para renombrar la vista en la base de datos y en admin de la pagina web
        verbose_name='Categoria'
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.nombre

class Post (models.Model):
    titulo= models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen= models.ImageField(upload_to='blog', null= True, blank=True) # null= True, blank=True)  para indicar que es opcional subir la imagen
    autor=models.ForeignKey(User, on_delete= models.CASCADE)# PARA VINCULAR  CON CLAVE FORANEA CON EL USUARIO Y APLICAR CAMBIOS EN CASCADA
    categorias= models.ManyToManyField(Categoria)
    created= models.DateTimeField(auto_now_add=True)# para que se inicie con la fecha en el que se crea de forma automatica
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:

        #para renombrar la vista en la base de datos y en admin de la pagina web

        verbose_name='Post'
        verbose_name_plural='Post'

    def __str__(self):
        return self.titulo
