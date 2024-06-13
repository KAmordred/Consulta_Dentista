from django.shortcuts import render

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



# Create your views here.
