from django.contrib import admin
from .models import Producto, Contacto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'nuevo', 'marca','precio')
    list_editable = ('precio',)


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'tipo_consulta')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto, ContactoAdmin)


# Register your models here.

