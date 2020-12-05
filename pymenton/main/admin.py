from django.contrib import admin

from main.models import Usuario, Producto

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display=("nombre", "nombre_pyme","direccion","instagram")
    search_fields=("nombre", "nombre_pyme","direccion","instagram")

class ProductoAdmin(admin.ModelAdmin):
    list_display=("nombre","marca","precio")
    search_fields=("nombre","marca","precio")




admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Producto, ProductoAdmin)

