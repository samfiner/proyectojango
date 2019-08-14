from django.urls import path
from .views import saludar, nuevococinero,consultarpedidos,consultarchip,consultarnombre,consultarapellido

urlpatterns = [
    path('', saludar),
    path('nuevo/cocinero',nuevococinero ),
    path('pedido/',consultarpedidos ),
    path('chip/', consultarchip ),
    path('nombre/', consultarnombre ),
    path('apellido/', consultarapellido),
    
]
