from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    respu= "<ul>"
    respu=  respu +"<li>Elemento 1 </li>"
    respu=  respu +"<li>Elemento 2  </li>"
    respu=  respu +"<li></li>"
    return HttpResponse(respu)
def nuevococinero(request):
    return HttpResponse("<p> Esta es la pagina del nuevo cocinero</p>")

def consultarpedidos(request):
    return HttpResponse("<p> encuentra los mejores platos</p>")

def consultarchip(request):
     respu=  "<h1> CHIP IMPLATADO EN HUMANOS</h1>"
     respu= respu +"<h2> Este es uno de los nuevos inventos que cada vez es más popular en Europa y que promete revolucionar la manera en que hacemos nuestras compras </h2>"
     return HttpResponse(respu)

def consultarnombre(request):
   
    return HttpResponse("<p> lina </p>")

def consultarapellido(request):
    return HttpResponse("<p> baño </p>")
