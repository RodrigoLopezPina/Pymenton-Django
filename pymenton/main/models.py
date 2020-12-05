from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    nombre_pyme = models.CharField(max_length=50, unique=True)
    categoria = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50, unique=True)
    correo = models.EmailField(max_length=50, unique=True)
    instagram = models.CharField(max_length=50, unique=True)
    numero = models.IntegerField(max_length=9, unique=True)
    
    def get_prep_value(self, categoria):
        return str(categoria).lower()

    def __str__(self):
        return self.nombre_pyme

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    precio = models.IntegerField(max_length=9)

    def __str__(self):
        return self.nombre
