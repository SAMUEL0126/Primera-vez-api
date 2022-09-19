from django.db import models

# Create your models here.
class Persona(models.Model):
    imagen=models.ImageField()
    descripcion=models.TextField(max_length=200)
    tatuador=models.CharField(max_length=50)
    fecha_publicacion=models.DateField()


    