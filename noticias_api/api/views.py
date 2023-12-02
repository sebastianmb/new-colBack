from django.views import View
from django.http.response import JsonResponse
#Models
from .models import News
# Create your views here.


class NewsView(View):
    def get(self,request):
        noticias=list(News.objects.values())
        if len(noticias)>0:
            datos={'message':"Success",'noticias':noticias}
        else:
            datos={'message':'Noticias no encontradas...'}
        return JsonResponse(datos)
    def post(self,request):
        pass
    def put(self,request):
        pass
    def deleted(self,request):
        pass    
