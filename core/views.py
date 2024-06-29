from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm
from .models import Producto



# Create your views here.
def index(request):
    return render(request, 'index.html')

def contactanos(request):
    return render(request, 'contactanos.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def especialidades(request):
    return render(request, 'especialidades.html')

def insumos(request):
    return render(request, 'insumos.html')

def sillones(request):
    return render(request, 'sillones.html')

def venta_equipos_rx(request):
    return render(request, 'AVentaEquiposRX.html')

def venta_sillas(request):
    return render(request, 'AVentaSillas.html')

def venta_sillones_full(request):
    return render(request, 'AVentaSillonesFull.html')

def venta_sillones_viejos(request):
    return render(request, 'AVentaSillonesViejos.html')

def venta_implantes(request):
    return render(request, 'BVentaImplantes.html')

def venta_instrumentos(request):
    return render(request, 'BVentaInstrumentos.html')

def venta_kit_completo(request):
    return render(request, 'BVentaKitCompleto.html')

def venta_resinas(request):
    return render(request, 'BVentaResinas.html')

def despacho(request):
    return render(request, 'despacho.html')

def detalle_producto(request,pk):
    producto = get_object_or_404(producto,pk=pk)
    return render(request,'detalle_producto.html',{'producto': producto})

def editar_producto(request,pk):
    producto = get_object_or_404(producto,pk=pk)
    if request.method == "POST":
        form = productoform(request.POST, request.FILES, isinstance=producto)
        if form.is_valid():
            producto = form.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = productoform(isinstance=producto)
    return render(request,'editar_producto.html' , {'form' : form})

def lista_producto(request):
    productos =Producto.objects.all()
    return render(request,'lista_producto.html', {'productos': productos})

def nuevo_producto (request):
    if request.method =="POST":
        form = productoform(reqest.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = productoform(isinstance=producto)
    return render(request,'editar_producto.html' , {'form' : form})


def eliminar_producto(request, pk):
    producto = get_object_or_404(producto , pk=pk)
    producto.delete()
    return redirect('lista_productos')

#Metodo de vista para manejar login.
def login_vista(request):

    error = None

    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contra = request.POST.get('password')   

        user = authenticate(username = usuario, password = contra)

        if user is None:
            error = 'Error: Las credenciales de acceso no son validas'
        else:
            login(request, user)
            return redirect('index')

    return render(request, 'login.html',{"error":error})

#Proteger las vistas requeridas con el decorador, para que solo los usuarios autenticados puedan acceder.
@login_required
def comprar(request):
    return render(request, 'comprar.html')

@login_required
def reservar(request):
    return render(request, 'reservar.html')
# Lógica para procesar la reserva y la compra (Return)