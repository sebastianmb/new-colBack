from typing import Any
from django import http
from django.views import View
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
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
        datos={'message':"Success"}
        return JsonResponse(datos)
    def put(self,request):
        pass
    def deleted(self,request):
        pass    
