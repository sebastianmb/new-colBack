from typing import Any
from django import http
from django.views import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
#Models
from .models import News
# Create your views here.


class NewsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs ): 
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,id=0):
        if(id>0):
            noticias=list(News.objects.filter(id=id).values())
            if len(noticias)>0:
                noticia=noticias[0]
                datos={'message':"Success", 'noticia': noticia }
            else:
                datos={'message':"Noticia no encontrada" }
            
            return JsonResponse(datos)

        
        else:
            noticias=list(News.objects.values())
            if len(noticias)>0:
                datos={'message':"Success",'noticias':noticias}
            else:
                datos={'message':'Noticias no encontradas...'}
            return JsonResponse(datos)
    def post(self,request):
        # Obtener los datos del formulario o solicitud POST
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')
        tags = request.POST.get('tags')
        image_file = request.FILES.get('image')  # Acceso al archivo de imagen

        # Guardar el objeto News con la imagen
        news = News.objects.create(
            title=title,
            content=content,
            author=author,
            published_date=published_date,
            tags=tags,
            image=image_file  # Asignar la imagen al campo 'image' del modelo News
        )

        return JsonResponse({'message': 'Datos recibidos correctamente'})
    
    def put(self,request, id):

        jd=json.loads(request.body)
        noticias=list(News.objects.filter(id=id).values())
        if len(noticias)>0:
            noticia= News.objects.get(id=id)
            noticia.title=jd['title']
            noticia.content=jd['content']
            noticia.author=jd['author']

            noticia.save()
            datos={'message':'Success'}

        else:
            datos={'message':'Noticia no encontrada...'}
        
        return JsonResponse(datos)
    def delete(self,request, id):
        
        noticias=list(News.objects.filter(id=id).values())
        if len(noticias)>0:
            noticia= News.objects.filter(id=id).delete()
            datos={'message':'Success'}
        else:
            datos={'message':'Noticia no encontrada...'}
        return JsonResponse(datos)

