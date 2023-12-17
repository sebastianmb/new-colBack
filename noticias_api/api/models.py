from django.db import models



class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField()
    

    
 
    tags = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='news/')
    def get_image_url(self):
            if self.image:
                return self.image.url
            else:
                return None  # Opcional: puedes devolver una URL predeterminada si no hay imagen
    def __str__(self):
        return self.title
