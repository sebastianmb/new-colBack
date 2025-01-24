from django.db import models
from cloudinary.models import CloudinaryField



class News(models.Model):
    title = models.CharField(max_length=255)
    # Nuevos campos
    audio = models.FileField(upload_to='news/audio/', blank=True, null=True)  # Campo para el archivo de audio
    titulo_leccion_gramatica = models.CharField(max_length=255, blank=True)
    descripcion_gramatica = models.TextField(blank=True)
    palabras_a_buscar = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField()
    

    
 
    tags = models.CharField(max_length=255, blank=True)
    imagen = CloudinaryField('imagen',blank=True, null=True)
    def get_image_url(self):
            if self.image:
                return self.image.url
            else:
                return None  # Opcional: puedes devolver una URL predeterminada si no hay imagen
    def __str__(self):
        return self.title
