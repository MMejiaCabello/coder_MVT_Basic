from django.db import models

# Create your models here.
class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    relacion = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()
    email = models.CharField(max_length=20)
    profesion = models.CharField(max_length=20)