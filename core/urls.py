from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contactanos/', views.contactanos, name='contactanos'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('especialidades/', views.especialidades, name='especialidades'),
    path('insumos/', views.insumos, name='insumos'),
    path('VentaEquiposRX/', views.venta_equipos_rx, name='AVentaEquiposRX'),
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

    path('productos/', views.lista_producto, name = 'lista_producto'),
    path('productos/nuevo/', views.nuevo_producto, name ='nuevo_producto'),
    path('productos/<int:pk>/', views.detalle_producto, name = 'detalle_producto'),
    path('productos/<int:pk>/editar/', views.editar_producto, name ='editar_producto'),
    path('productos/<int:pk>/eliminar/', views.eliminar_producto, name ='eliminar_producto'),
    
]
