from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='news_images/')  # Campo para la imagen

    def __str__(self):
        return self.title