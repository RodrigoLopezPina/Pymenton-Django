from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index, name="index"),
    #path("home/login/", views.login, name="login"),
    path("home/quienes_somos/", views.quienes_somos, name="quienes_somos"),
<<<<<<< Updated upstream
=======
    path("quienes_somos2/", views.quienes_somos2, name="quienes_somos2"),
    path("resultado_busqueda/", views.resultado_busqueda),
    path("resultado_busqueda2/", views.resultado_busqueda2),
    path("resultado_busqueda3/", views.resultado_busqueda3),
    path("resultado_busqueda4/", views.resultado_busqueda4),
    path("contacto/", views.contacto),
    path("registrar/", RegistroUsuario.as_view(), name="registrar"),
    path('loginn/', views.login),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("h0me/", views.index2, name="index2"),
    path("registropyme/", views.RegistroPyme, name='registropyme'),
    path("vermas/", views.vermas, name='vermas'),
    path("v3rmas/", views.vermas2, name='vermas2'),
>>>>>>> Stashed changes
]

