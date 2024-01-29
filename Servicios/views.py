from django.shortcuts import render
from Servicios.models import Servicio

def servicios(request):

  servicio= Servicio.objects.all()

  return render(request, 'Servicios/servicios.html',{"servicios": servicio})
