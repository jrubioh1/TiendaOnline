from django.shortcuts import render, redirect
from Contacto.forms import FormularioContacto
from django.core.mail  import EmailMessage

# Create your views here.
def contacto(request):
  
  formulario_contacto= FormularioContacto()

  if request.method == "POST":

    formulario_contacto=FormularioContacto(request.POST)

    if formulario_contacto.is_valid():
      nombre=request.POST.get('nombre')
      email=request.POST.get('email')
      contenido=request.POST.get('contenido')

    #NO FUNCIONA SERVIDOR DEL EMAIL ME RECHAZA
      email=EmailMessage("Mensaje desde AppDjango",
      f'''El usuario con nombre {nombre} con la direccion{email} escribe:
            {contenido}
      ''',
      '',
      ['aguabrava_jo@hotmail.com'],
      reply_to=[email]
      
       )

    
      try:
        email.send()
      except:
         return redirect('/contacto/?novalido')
      return redirect('/contacto/?valido')


  return render(request, 'Contacto/contacto.html', {"formulario": formulario_contacto})

