from django.db import models

    # Definimos la clase producto y que sera un tipo de modelo de Django (tipo especial para crear bases de datos).
    # Definimos los atributos:
    # (models.CharField) almacenara datos con una longitud maxima de 255 caracteres.
    # (models.TextField) esto es para almacenar grandes cantidades de texto.
    # (models.DecimalField(max_digits=10, decimal_places=2) almacena los precios de los productos como valores decimales.
    # (models.PositiveIntegerField) restringe los valores a enteros no negativos.
    # (models.ImageField) almacenará las rutas de los archivos de imagen.
    # - upload_to='productos/' especifica un directorio donde se cargarán las imágenes del producto.
    # - blank=True, null=True permite productos sin imagen (opcional)

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    #ID: no es necesario crearlo ya que lo crea django
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    nuevo = models.BooleanField(default=False)
    marca = models.CharField(max_length=100, default='Desconocida')
    cantidad_disponible = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    productos = models.ManyToManyField(Producto, through='DetallePedido')
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido #{self.id} - {self.fecha_pedido}"


class DetallePedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de Pedido #{self.pedido.id} - {self.producto.nombre}"

# Formulario de contacto de Django
opciones_consultas = [
    [0, "Solicitud de cita"],
    [1, "Solicitud de información sobre servicios"],
    [2, "Consulta sobre tratamientos específicos"],
    [3, "Solicitud de presupuesto"],
    [4, "Realizar una consulta"]    
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50) #Guardar datos de texto con un maximo de 50 caracteres
    correo = models.EmailField()  #Para la validacion del Email
    tipo_consulta = models.IntegerField(choices=opciones_consultas) #para definir las opciones del formulario con numeros, que llamaremos en un arreglo
    mensaje = models.TextField() #para definir un mensaje escrito por el usuario
    avisos = models.BooleanField() #Si quiere recibir avisos

    def __str__(self):
        return self.nombre
