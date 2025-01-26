from rest_framework import serializers
from .models import News

class NewsSerializer(serializers.ModelSerializer):
    # Para asegurar que la imagen sea convertida a una URL accesible
    imagen = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = [
            'id', 'title', 'audio','audio_url', 'titulo_leccion_gramatica', 
            'descripcion_gramatica', 'palabras_a_buscar', 'content', 
            'author', 'published_date', 'tags', 'imagen'
        ]

    def get_imagen(self, obj):
        # Si la imagen existe, devuelve la URL, si no, devuelve None
        if obj.imagen:
            return obj.imagen.url
        return None
    def get_audio_url(self, obj):
        # Llamar al método get_audio_url de tu modelo para obtener la URL correcta
        return obj.get_audio_url()  # Asegúrate de que el método get_audio_url exista en tu modelo
