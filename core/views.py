from django.shortcuts import render, redirect, get_object_or_404
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
    productos = Producto.objects.all()
    return render(request, 'insumos.html', {'productos': productos})
# logica para obtener los productos desde la base de datos

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
            return redirect('lista_producto')  # Ajustar 'lista_producto' al nombre correcto de la ruta
    else:
        form = ProductoForm()
    return render(request, 'agregar.html', {'form': form})

def listar_producto(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def detalle_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, 'detalle.html', {'producto': producto})

def editar_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('detalle_producto', pk=pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar.html', {'form': form})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('lista_producto')


def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id=id)

    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method =='POST':
        formulario = ProductoForm(data = request.POST, instance=producto, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='lista_producto')
        data["form"] = formulario

    return render(request, 'modificar.html',data)

def login_vista(request):
    error = None
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contra = request.POST.get('password')
        user = authenticate(username=usuario, password=contra)
        if user is None:
            error = 'Error: Las credenciales de acceso no son válidas'
        else:
            login(request, user)
            return redirect('insumos')
    return render(request, 'login.html', {"error": error})

def logout_vista(request):
    logout(request)
    return redirect('index')

@login_required
def comprar(request):
    return render(request, 'comprar.html')

@login_required
def reservar(request):
    return render(request, 'reservar.html')
