from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from main.models import Usuario, Producto

# Create your views here.

def index(response):
    return render(response, "main/index.html")

def login(response):
    return render(response, "main/login2.html")

def quienes_somos(response):
    return render(response, "main/quienes_somos.html")

def resultado_busqueda(request):

    if request.GET["prd"]:
        
        #mensaje= "Pyme buscada: %r" %request.GET["prd"]
        pyme=request.GET["prd"]

        if len(pyme)>20:
            mensaje= "Texto de búsqueda demasiado largo."

        else:

            lista_pyme=Usuario.objects.filter(nombre_pyme__icontains=pyme)
            print(lista_pyme)
        

        return render(request, "main/resultados.html",{"lista_pyme":lista_pyme, "query":pyme} )

    else:
        mensaje = "No has introducido nada"

    return HttpResponse(mensaje)


def resultado_busqueda2(request):

    if request.GET["prb"]:
        
        #mensaje= "Pyme buscada: %r" %request.GET["prd"]
        pyme=request.GET["prb"]

        if len(pyme)>20:
            mensaje= "Texto de búsqueda demasiado largo."

        else:

            lista_pyme=Usuario.objects.filter(categoria__icontains=pyme)
        

        return render(request, "main/resultados.html",{"lista_pyme":lista_pyme, "query":pyme} )

    else:
        mensaje = "No has introducido nada"

    return HttpResponse(mensaje)    

def contacto (request):
    return render(request, "contacto.html")
