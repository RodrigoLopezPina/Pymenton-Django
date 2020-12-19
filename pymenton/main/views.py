from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, Context, loader
from main.models import Usuario, Producto
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm, UsuarioForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.

def index(response):
    return render(response, "main/index.html")

def index2(response):
    return render(response, "main/index2.html")

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



class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('index')

def RegistroPyme(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect ("/h0me")
    else:
        form = UsuarioForm()
    return render(request, 'usuario/registrar_pyme.html', {'form':form})

def loginn(response):
    return render(response, "loginn.html")
    