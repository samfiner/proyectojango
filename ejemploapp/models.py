from django.db import models

class Libro(models.Model):
    nombre=models.CharField(max_length=45)
    descripcion=models.CharField(max_length=45)
    isbn=models.CharField(max_length=45)
    copias=models.IntegerField(null=True)

    def __str__(self):
        return self.nombre

class Prestamo (models.Model):
    fecha_prestamo=models.DateField(max_length=45)
    nombre_cliente=models.CharField(max_length=45)
    telefono_cliente=models.CharField(max_length=45)
    estado=models.BooleanField(default=True, editable=False)
  

class Ejemplar(models.Model):
    numero_ejemplar=models.CharField(max_length=45)
    fecha_de_compra=models.DateField(max_length=45, null = True)
    Libro= models.ForeignKey(Libro, on_delete=models.CASCADE )

class detalleprestamo(models.Model):
     prestamo=  models.ForeignKey(Prestamo, on_delete=models.CASCADE )
     ejemplar=  models.ForeignKey(Ejemplar, on_delete=models.CASCADE )


  
  
    
   

    
   

