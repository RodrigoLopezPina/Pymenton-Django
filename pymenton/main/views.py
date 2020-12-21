from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
<<<<<<< Updated upstream
=======
from main.models import Usuario, Producto
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm, UsuarioForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login as alexis

>>>>>>> Stashed changes

# Create your views here.

def index(response):
    return render(response, "main/index.html")

<<<<<<< Updated upstream
def login(response):
    return render(response, "main/login.html")

def quienes_somos(response):
    return render(response, "main/quienes_somos.html")
=======
def index2(response):
    return render(response, "main/index2.html")


def quienes_somos(response):
    return render(response, "main/quienes_somos.html")

def quienes_somos2(response):
    return render(response, "main/quienes_somos2.html")    

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

def resultado_busqueda3(request):
    
    if request.GET["prd"]:
        
        #mensaje= "Pyme buscada: %r" %request.GET["prd"]
        pyme=request.GET["prd"]

        if len(pyme)>20:
            mensaje= "Texto de búsqueda demasiado largo."

        else:

            lista_pyme=Usuario.objects.filter(nombre_pyme__icontains=pyme)

        return render(request, "main/resultados2.html",{"lista_pyme":lista_pyme, "query":pyme} )

    else:
        mensaje = "No has introducido nada"

    return HttpResponse(mensaje)


def resultado_busqueda4(request):

    if request.GET["prb"]:
        
        #mensaje= "Pyme buscada: %r" %request.GET["prd"]
        pyme=request.GET["prb"]

        if len(pyme)>20:
            mensaje= "Texto de búsqueda demasiado largo."

        else:

            lista_pyme=Usuario.objects.filter(categoria__icontains=pyme)
        

        return render(request, "main/resultados2.html",{"lista_pyme":lista_pyme, "query":pyme} )

    else:
        mensaje = "No has introducido nada"

    return HttpResponse(mensaje)  

def contacto (request):
    return render(request, "main/contacto.html")



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
            return redirect ("/registropyme")
    else:

        form = UsuarioForm()
    return render(request, 'usuario/registrar_pyme.html', {'form':form})

def login(request):
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(request, username=_username, password=_password)
        if user is not None:
            alexis(request, user)
            return redirect('/h0me')
        else:
            messages.error(request, 'Usuario o Contraseña Incorrecta!')  # this will be shown as pop-up message
            return render(request, 'loginn.html')
    elif request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/h0me')
        else:
            return render(request, 'loginn.html')

def vermas(request):
    if request.GET["namepyme"]:
        
        #mensaje= "Pyme buscada: %r" %request.GET["prd"]
        pyme=request.GET["namepyme"]

        if len(pyme)>2000:
            mensaje= "Texto de búsqueda demasiado largo."

        else:

            lista_pyme=Usuario.objects.filter(nombre_pyme__icontains=pyme)

        return render(request, "main/vermas.html",{"lista_pyme":lista_pyme, "query":pyme} )

    else:
        mensaje = "No has introducido nada"

    return HttpResponse(mensaje)


def vermas2(request):
    if request.GET["namepyme"]:
        
        #mensaje= "Pyme buscada: %r" %request.GET["prd"]
        pyme=request.GET["namepyme"]

        if len(pyme)>2000:
            mensaje= "Texto de búsqueda demasiado largo."

        else:

            lista_pyme=Usuario.objects.filter(nombre_pyme__icontains=pyme)

        return render(request, "main/vermas2.html",{"lista_pyme":lista_pyme, "query":pyme} )

    else:
        mensaje = "No has introducido nada"

    return HttpResponse(mensaje)
>>>>>>> Stashed changes
