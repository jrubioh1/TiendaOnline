from django.urls import path
from Autenticacion.views import VRegistro,cerrar_sesion, logear


urlpatterns=[  
    path('', VRegistro.as_view(), name='Autenticacion'), #esta convirtiendo la clase en  una vista
    path('cerrar_sesion/', cerrar_sesion, name='CerrarSesion'),
    path('logear/', logear, name='Logear'),
]
