from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.storage import RawMediaCloudinaryStorage




class News(models.Model):
    title = models.CharField(max_length=255)
    # Nuevos campos
   # Almacenar audio en Cloudinary como archivo raw
    audio = models.FileField(
        upload_to='audios/',
        storage=RawMediaCloudinaryStorage(),
        blank=True,
        null=True
    )
    titulo_leccion_gramatica = models.CharField(max_length=255, blank=True)
    descripcion_gramatica = models.TextField(blank=True)
    palabras_a_buscar = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField()
    

    
 
    tags = models.CharField(max_length=255, blank=True)
    imagen = CloudinaryField('imagen',blank=True, null=True)

    def get_image_url(self):
        """ Devuelve la URL de la imagen almacenada en Cloudinary """
        if self.imagen:
            return self.imagen.url
        return None  # O podrías devolver una URL predeterminada

    def get_audio_url(self):
        """ Devuelve la URL del archivo de audio almacenado en Cloudinary """
        if self.audio:
            # Reemplazar 'image/upload' por 'raw/upload' para la URL de audio
            audio_url = self.audio.url.replace("image/upload", "raw/upload")
            return audio_url
        return None  # O podrías devolver un mensaje indicando que no hay audio


    def __str__(self):
        return self.title