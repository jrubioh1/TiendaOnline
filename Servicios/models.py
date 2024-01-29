from django.db import models

class Servicio(models.Model):
    titulo= models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen= models.ImageField(upload_to='servicios')
    created= models.DateTimeField(auto_now_add=True)# para que se inicie con la fecha en el que se crea de forma automatica
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:

        #para renombrar la vista en la base de datos y en admin de la pagina web

        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo


   
