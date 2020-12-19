from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import *
from django import forms

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'username': 'Nombre de Usuario',
        'first_name': 'Nombre',
        'last_name': 'Apellidos',
        'email': 'Correo',
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','nombre_pyme','categoria','direccion','correo','instagram','numero']
        labels = {'nombre':'Nombre',
        'nombre_pyme':'Nombre de tu PYME',
        'categoria':'Categorias',
        'direccion':'Dirección',
        'correo':'Correo',
        'instagram':'Instagram',
        'numero':'Teléfono',
        }
        '''widgets = {
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
        'nombre_pyme':forms.TextInput(attrs={'class':'form-control'}),
        'categoria':forms.TextInput(attrs={'class':'form-control'}),
        'direccion':forms.TextInput(attrs={'class':'form-control'}),
        'correo':forms.TextInput(attrs={'class':'form-control'}),
        'instagram':forms.TextInput(attrs={'class':'form-control'}),
        'numero':forms.TextInput(attrs={'class':'form-control'}),
        }'''

        
