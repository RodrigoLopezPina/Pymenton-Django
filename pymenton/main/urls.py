from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from main.views import RegistroUsuario
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("home/", views.index, name="index"),
    path("home/login/", views.login, name="login"),
    path("home/quienes_somos/", views.quienes_somos, name="quienes_somos"),
    path("resultado_busqueda/", views.resultado_busqueda),
    path("resultado_busqueda2/", views.resultado_busqueda2),
    path("contacto/", views.contacto),
    path("registrar/", RegistroUsuario.as_view(), name="registrar"),
    path('loginn/', LoginView.as_view(template_name='loginn.html'), name="loginn"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("h0me/", views.index2, name="index2"),
    path("registropyme/", views.RegistroPyme, name='registropyme')
]
