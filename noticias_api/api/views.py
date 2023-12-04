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
    def get(self,request):
        noticias=list(News.objects.values())
        if len(noticias)>0:
            datos={'message':"Success",'noticias':noticias}
        else:
            datos={'message':'Noticias no encontradas...'}
        return JsonResponse(datos)
    def post(self,request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        News.objects.create(title=jd['title'],content=jd['content'],author=jd['author'],published_date=jd['published_date'],tags=jd['tags'])
        datos={'message':"Success"}
        return JsonResponse(datos)
    def put(self,request):
        pass
    def deleted(self,request):
        pass    
