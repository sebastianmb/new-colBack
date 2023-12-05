from django.urls import path

#Views
from .views import NewsView

urlpatterns=[
    path('noticias/',NewsView.as_view(), name='noticias_list'),
    path('noticias/<int:id>',NewsView.as_view(), name='noticias_process'),
]