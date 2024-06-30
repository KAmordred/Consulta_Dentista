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


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirigir a la página principal o a donde necesites después de guardar
            return redirect('agregar_producto')  # Ajusta 'home' al nombre de tu ruta de redirección
    else:
        form = ProductoForm()

    return render(request, 'agregar.html', {'form': form})



def listar_producto(request):
    productos = Producto.objects.all()

    data = {
        'productos' : productos
    }
    return render(request, 'listar.html',data)



#Metodo de vista para manejar login
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
            return redirect('insumos')

    return render(request, 'login.html',{"error":error})

#Proteger las vistas requeridas con el decorador, para que solo los usuarios autenticados puedan acceder.
@login_required
def comprar(request):
    return render(request, 'comprar.html')

@login_required
def reservar(request):
    return render(request, 'reservar.html')
# Lógica para procesar la reserva y la compra (Return)