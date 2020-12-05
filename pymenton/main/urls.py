from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    path("home/login/", views.login, name="login"),
    path("home/quienes_somos/", views.quienes_somos, name="quienes_somos"),
    path("resultado_busqueda/", views.resultado_busqueda),
    path("resultado_busqueda2/", views.resultado_busqueda2),
    path("contacto/", views.contacto),
    
]

