from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    nombre_pyme = models.CharField(max_length=50, unique=True)
    categoria = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50, unique=True)
    correo = models.EmailField(max_length=50, unique=True)
    instagram = models.CharField(max_length=50, unique=True)
    numero = models.IntegerField(unique=True)

    
    def get_prep_value(self, categoria):
        return str(categoria).lower()

    def __str__(self):
        return self.nombre_pyme

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField()
    usuario = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
