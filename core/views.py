from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm, CustomUserCreationForm, ContactoForm
from .models import Producto, Despacho, Region
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets
from .serializers import DespachoSerializer


# views.py Sirve para concectarse con el modelo django, definir procesos con Python y encontrar el template para mostrar al usuario.

# render: Es el proceso de generar y mostrar contenido visual en una pantalla a partir de datos y plantillas o modelos
# request: Respuesta, la solicitud HTTP que se está procesando. Es un objeto HttpRequest que Django pasa automáticamente a las vistas.   
# Se crea una funcion (def)nombre(request): lo que hace es encontrar el template(el html) y lo devuelve el request con render 

# Create your views here. 

def index(request):
    return render(request, 'index.html')

def contactanos(request):
    data = {
        'form': ContactoForm() #Se define la varia form que sera igual a un nuevo contacto form, crea una instancia con el formulario vacio
    }

    if request.method == 'POST':  # Si el método es POST, significa que se enviaron datos
        formulario = ContactoForm(data=request.POST)  # Llenamos el formulario con los datos enviados en request.POST
        if formulario.is_valid():  # Verificamos si el formulario es válido
            formulario.save()  # Si es válido, guardamos el formulario
            messages.success(request, "Enviado Correctamente")
            data["mensaje"] = "Contacto enviado"  # Añadimos un mensaje de éxito a data
        else:  # Si el formulario no es válido
            data["form"] = formulario  # Sobrescribimos el formulario en data con los datos enviados para mostrar los errores


    return render(request, 'contactanos.html',data) #Se debe enviar el data, por lo que se pasa como 3er parametro.

# Wiew para agragar productos al admin Django
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto agregado correctamente")
            # Redirigir a la página principal o a donde necesites después de guardar
            return redirect('lista_producto')  # Ajusta 'lista_producto' al nombre correcto de la ruta
    else:
        form = ProductoForm()    
    return render(request, 'agregar.html', {'form': form})

# Wiew para listar los productos al admin Django
def listar_producto(request):
    productos_list = Producto.objects.all()  # Obtiene todos los productos de la base de datos
    paginator = Paginator(productos_list, 4)  # Mostrar 4 productos por página

    page = request.GET.get('page')
    try:
        productos = paginator.page(page)  # Obtiene los productos para la página solicitada
    except PageNotAnInteger:
        # Si el parámetro de la página no es un número, muestra la primera página
        productos = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera del rango, muestra la última página
        productos = paginator.page(paginator.num_pages)
    return render(request, 'listar.html', {'productos': productos})  # Renderiza la plantilla con los productos paginados

# Wiew para modificar los los productos desde el admin Django
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id) #get_object_or_404, busca un producto o elemento

    data = {
        'form': ProductoForm(instance=producto) #Inicializar el formulario con los datos del producto existente
    }

    if request.method =='POST':
        formulario = ProductoForm(data = request.POST, instance=producto, files= request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect('lista_producto')
        data["form"] = formulario
    return render(request, 'modificar.html', data)

# View para eliminar los productos
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")  # Mensaje de éxito al eliminar
    return redirect('lista_producto')

def detalle_producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    return render(request, 'detalle.html', {'producto': producto})

# Funcion para modificar o editar el producto en la vista listar
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

#View para el manejo del login
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

#Views de registro de usuario
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    formulario = CustomUserCreationForm(data = request.POST)
    if formulario.is_valid():
        formulario.save()
        user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
        login(request,user)
        messages.success(request,"Te has registro correctamente")
        return redirect(to ='index')
    data["form"] = formulario
    return render(request, 'registration/registro.html',data)

#Desloguearse y regresar a vista principal
def logout_vista(request):
    logout(request)
    return redirect('index')

#View para manejar el carrito de compras
def agregar_al_carrito(request, id):
    producto = get_object_or_404(Producto, id=id)
    carrito = request.session.get('carrito', {})

    if str(producto.id) in carrito:
        if carrito[str(producto.id)]['cantidad'] < producto.cantidad_disponible:
            carrito[str(producto.id)]['cantidad'] += 1
            producto.cantidad_disponible -= 1
            producto.save()
            messages.success(request, "Producto agregado correctamente")
        else:
            messages.error(request, "No hay suficiente stock disponible")
    else:
        if producto.cantidad_disponible > 0:
            carrito[str(producto.id)] = {
                'nombre': producto.nombre,
                'precio': float(producto.precio),
                'marca': producto.marca,
                'cantidad': 1,
                'imagen_url': producto.imagen.url if producto.imagen else None,
                'stock': producto.cantidad_disponible - 1
            }
            producto.cantidad_disponible -= 1
            producto.save()
            messages.success(request, "Producto agregado correctamente")
        else:
            messages.error(request, "No hay suficiente stock disponible")

    request.session['carrito'] = carrito
    return redirect('insumos')

# proteccion de las vistas que necesitan autenticacion con decorador @login_required
@login_required
def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    costo_despacho = None  # Inicialmente None
    region_id = direccion = ciudad = codigo_postal = None

    if request.method == 'POST':
        region_id = request.POST.get('region')
        direccion = request.POST.get('direccion')
        ciudad = request.POST.get('ciudad')
        codigo_postal = request.POST.get('codigo_postal')
        
        if region_id:
            region = get_object_or_404(Region, pk=region_id)
            region_ordinal = region.ordinal  # Obtener el ordinal como está en el modelo
            costo_despacho = 4500  # Costo base para la Región Metropolitana

            # Calcular el costo de despacho basado en el ordinal
            if region_ordinal == 'XV':
                costo_despacho += 1500 * 6
            elif region_ordinal == 'I':
                costo_despacho += 1500 * 5
            elif region_ordinal == 'II':
                costo_despacho += 1500 * 4
            elif region_ordinal == 'III':
                costo_despacho += 1500 * 3
            elif region_ordinal == 'IV':
                costo_despacho += 1500 * 2
            elif region_ordinal == 'VI':
                costo_despacho += 1500 * 1
            elif region_ordinal == 'VII':
                costo_despacho += 1500 * 2
            elif region_ordinal == 'VIII':
                costo_despacho += 1500 * 3
            elif region_ordinal == 'IX':
                costo_despacho += 1500 * 4
            elif region_ordinal == 'XIV':
                costo_despacho += 1500 * 5
            elif region_ordinal == 'X':
                costo_despacho += 1500 * 6
            elif region_ordinal == 'XI':
                costo_despacho += 1500 * 7
            elif region_ordinal == 'XII':
                costo_despacho += 1500 * 8

    subtotal = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    iva = subtotal * 0.19
    total = subtotal + iva + (costo_despacho if costo_despacho else 0)

    context = {
        'carrito': carrito,
        'subtotal': subtotal,
        'iva': iva,
        'total': total,
        'costo_despacho': costo_despacho,
        'regiones': Region.objects.all(),
        'region_id': region_id,
        'direccion': direccion or '',
        'ciudad': ciudad or '',
        'codigo_postal': codigo_postal or ''
    }

    return render(request, 'carrito.html', context)

@login_required
def eliminar_del_carrito(request, id):
    carrito = request.session.get('carrito', {})
    if str(id) in carrito:
        del carrito[str(id)]
    request.session['carrito'] = carrito
    messages.success(request, "Producto eliminado correctamente")
    return redirect('ver_carrito')

@login_required
def actualizar_cantidad(request, id):
    carrito = request.session.get('carrito', {})
    if str(id) in carrito:
        cantidad = int(request.POST.get('cantidad', 1))
        if cantidad > 0:
            carrito[str(id)]['cantidad'] = cantidad
        else:
            del carrito[str(id)]
    request.session['carrito'] = carrito
    return redirect('ver_carrito')

# Logica para obtener los productos desde la base de datos y mostrarlos en la vista de insumos.
# Se realiza la consulta de objetos y se transforman los datos en una lista de productos (instancias).
def insumos(request):
    productos_list = Producto.objects.all()  # Obtiene todos los productos de la base de datos
    paginator = Paginator(productos_list, 8)  # Mostrar 8 productos por página

    page = request.GET.get('page')
    try:
        productos = paginator.page(page)  # Obtiene los productos para la página solicitada
    except PageNotAnInteger:
        # Si el parámetro de la página no es un número, muestra la primera página
        productos = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera del rango, muestra la última página
        productos = paginator.page(paginator.num_pages)
    return render(request, 'insumos.html', {'productos': productos})  # Renderiza la plantilla con los productos paginados

#View para manejar vistas para mostrar los detalles de los productos
def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)  # Obtiene el producto o lanza un error 404 si no existe
    return render(request, 'detalle_producto.html', {'producto': producto})  # Renderiza la plantilla con los detalles del producto

def nosotros(request):
    return render(request, 'nosotros.html')

def especialidades(request):
    return render(request, 'especialidades.html')

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

#View para definir las vistas para la API
class DespachoViewSet(viewsets.ModelViewSet):
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerializer