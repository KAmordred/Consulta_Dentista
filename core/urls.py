from django.urls import path, include
from . import views

#url.py sirve para definir las rutas que se mostraran en el proyecto

# Path: funcion para definir una URL.
# wiews: vista que se ejecutará cuando alguien visite la pagina
# name= alias que se le asignara a la web

# URL: Un usuario escribe www.cepillin.cl/contactanos/ en su navegador.
# path: Django ve la configuración en path('contactanos/',views.contactanos,name='contactanos') y sabe que debe usar la función contactanos en views.py.
# Vista: La función contactanos en views.py se ejecuta y genera la página web usando la plantilla contactanos.html.
# Nombre de Ruta: Si en alguna parte de tu sitio quieres crear un enlace a esta página, puedes usar el nombre 'contactanos' en lugar de escribir 
#   la URL completa.

urlpatterns = [

    path('', views.index, name='index'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('especialidades/', views.especialidades, name='especialidades'),
    path('insumos/', views.insumos, name='insumos'),
    path('AVentaEquiposRX/', views.venta_equipos_rx, name='AVentaEquiposRX'),
    path('AVentaSillas/', views.venta_sillas, name='AVentaSillas'),
    path('AVentaSillonesFull/', views.venta_sillones_full, name='AVentaSillonesFull'),
    path('AVentaSillonesViejos/', views.venta_sillones_viejos, name='AVentaSillonesViejos'),
    path('BVentaImplantes/', views.venta_implantes, name='BVentaImplantes'),
    path('BVentaInstrumentos/', views.venta_instrumentos, name='BVentaInstrumentos'),
    path('BVentaKitCompleto/', views.venta_kit_completo, name='BVentaKitCompleto'),
    path('BVentaResinas/', views.venta_resinas, name='BVentaResinas'),
    path('sillones/', views.sillones, name='sillones'),
    path('despacho/', views.despacho, name='despacho'),
    path('login/', views.login_vista, name='login'),
    path('logout/', views.logout_vista, name='logout'),
    path('listar_producto/', views.listar_producto, name='lista_producto'),
    path('agregar_producto/', views.agregar_producto, name='nuevo_producto'),
    path('modificar-producto/<id>/',views.modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', views.registro, name="registro"),    
    path('comprar/', views.comprar, name='comprar'),
    path('reservar/', views.reservar, name='reservar'),
    path('producto/<int:id>/', views.detalle_producto, name='detalle_producto'), 
]
