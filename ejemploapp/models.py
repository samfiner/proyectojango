from django.db import models

class Libro(models.Model):
    nombre=models.CharField(max_length=45)
    descripcion=models.CharField(max_length=45)
    isbn=models.CharField(max_length=45)
