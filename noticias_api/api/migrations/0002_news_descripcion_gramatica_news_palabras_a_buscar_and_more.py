# Generated by Django 4.2.7 on 2025-01-08 18:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="descripcion_gramatica",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="news",
            name="palabras_a_buscar",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="news",
            name="titulo_leccion_gramatica",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]