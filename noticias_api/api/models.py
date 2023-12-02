from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField()
    

    
 
    tags = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return self.title
