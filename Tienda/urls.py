from django.urls import path
from Tienda import views
from django.conf import settings
from django.conf.urls.static  import static

urlpatterns=[  
    path('',views.tienda, name='Tienda'),
 
]

urlpatterns +=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) # para configurar la url para la busqueda de los media