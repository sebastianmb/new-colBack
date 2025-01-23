from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#Views
from .views import NewsView

urlpatterns=[
    path('noticias/',NewsView.as_view(), name='noticias_list'),
    path('noticias/<int:id>',NewsView.as_view(), name='noticias_process'),
    path('noticias/reciente', NewsView.as_view(), name='noticia_reciente'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Configuración para cargar imagenes

