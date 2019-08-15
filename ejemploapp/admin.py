from django.contrib import admin

from .models import Libro,Prestamo,Ejemplar,detalleprestamo
admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(Ejemplar)
admin.site.register(detalleprestamo)



