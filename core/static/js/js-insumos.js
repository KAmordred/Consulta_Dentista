const productosDentales = [
  { 
    nombre: "Equipo RX", 
    precio: 4499990, 
    imagen: "https://cdnx.jumpseller.com/buhos/image/31130732/resize/480/480?1685322796" 
  },
  { 
    nombre: "Full equipado ", 
    precio: 6190000, 
    imagen: "https://techdent.cl/wp-content/uploads/2024/04/SILLON-ORO.jpeg" 
  },
  { 
    nombre: "Full equipado usado", 
    precio: 1490000, 
    imagen: "https://img.clasf.mx/2020/11/28/Unidad-Dental-Compresor-y-Rayos-X-Todo-junto-20201128182606.8176110015.jpg" 
  },
  { 
    nombre: "Silla dental", 
    precio: 190000, 
    imagen: "https://i.pinimg.com/originals/e1/be/f9/e1bef91e28e4ff0b98fb84ee0ed9c535.jpg" 
  },
];

// Función para crear tarjetas de productos
function crearTarjetas() {
  const contenedorProductos = document.querySelector(".contenedor-productos");

  productosDentales.forEach(producto => {
    const card = document.createElement("div");
    card.classList.add("card");

    const imagen = document.createElement("img");
    imagen.src = producto.imagen;
    imagen.alt = producto.nombre;

    const contenido = document.createElement("div");
    contenido.classList.add("card-content");

    const nombre = document.createElement("h3");
    nombre.textContent = producto.nombre;

    const precio = document.createElement("p");
    precio.textContent = "Precio: $" + producto.precio.toFixed(1);

    const añadir = document.createElement("button");
    añadir.textContent = "Añadir al carrito";
    añadir.classList.add("boton");
    añadir.addEventListener("click", function() {
      agregarProductoAlCarrito(producto.nombre, producto.precio);
    });

    contenido.appendChild(nombre);
    contenido.appendChild(precio);
    contenido.appendChild(añadir);

    card.appendChild(imagen);
    card.appendChild(contenido);

    contenedorProductos.appendChild(card);
  });
}

// Función para agregar un producto al carrito
function agregarProductoAlCarrito(nombreProducto, precioProducto) {
  const listaCarrito = document.getElementById("lista-carrito");
  const item = document.createElement("li");

  const texto = document.createElement("span");
  texto.textContent = nombreProducto + " - $" + precioProducto.toFixed(1);

  const eliminar = document.createElement("button");
  eliminar.textContent = "Eliminar";
  eliminar.classList.add("boton-eliminar");
  eliminar.addEventListener("click", function() {
    eliminarProductoDelCarrito(item, precioProducto);
  });

  item.appendChild(texto);
  item.appendChild(eliminar);
  listaCarrito.appendChild(item);

  actualizarTotal(precioProducto);
  actualizarLocalStorage(); // Actualizar el localStorage al añadir

  // Actualizar el contenido del off-canvas
  actualizarOffCanvas();
}

// Función para eliminar un producto del carrito
function eliminarProductoDelCarrito(item, precioProducto) {
  item.remove();
  actualizarTotal(-precioProducto);
  actualizarLocalStorage(); // Actualizar el localStorage al eliminar

  // Actualizar el contenido del off-canvas
  actualizarOffCanvas();
}

// Función para actualizar el total del carrito
function actualizarTotal(precioProducto) {
  const totalElement = document.getElementById("total");
  let total = +totalElement.textContent.slice(8); // Obtener el valor numérico del total

  total += precioProducto;
  totalElement.textContent = "Total: $" + total.toFixed(1); // Actualizar el total en la página principal
}

// Función para simular el pago
function simularPago() {
  alert("Lo sentimos, el pago no está disponible en este momento.");
}

// Función para actualizar el off-canvas con los productos del carrito
function actualizarOffCanvas() {
  const listaCarrito = document.getElementById("lista-carrito");
  const items = listaCarrito.querySelectorAll("li");

  // Limpiar y volver a generar la lista en el off-canvas
  const offCanvasItems = document.getElementById("cart-items");
  offCanvasItems.innerHTML = "";
  
  items.forEach(item => {
    const listItem = document.createElement("li");
    listItem.textContent = item.querySelector("span").textContent;
    offCanvasItems.appendChild(listItem);
  });

  // Actualizar el total en el off-canvas
  const totalElement = document.getElementById("cart-total");
  totalElement.textContent = "Total: " + document.getElementById("total").textContent;
}

// Verificar si el usuario está autenticado
document.addEventListener("DOMContentLoaded", function() {
  const userAuthenticated = "{{ user.is_authenticated }}";

  if (userAuthenticated === 'True') {
    // Usuario autenticado: permitir funcionalidad completa
    crearTarjetas(); // Crear las tarjetas de productos al cargar la página
  } else {
    // Usuario no autenticado: mostrar mensaje de inicio de sesión
    const contenedorProductos = document.querySelector(".contenedor-productos");
    contenedorProductos.innerHTML = '<p>Por favor, inicia sesión para comprar productos.</p>';
  }

  // Cerrar el off-canvas al hacer clic en el botón de cerrar
  const closeOffcanvasBtn = document.querySelector("#offcanvasExample .btn-close");
  closeOffcanvasBtn.addEventListener("click", function() {
    const offcanvas = new bootstrap.Offcanvas(document.getElementById('offcanvasExample'));
    offcanvas.hide();
  });

  // Cargar el contenido del carrito desde localStorage
  cargarCarritoDesdeLocalStorage();
});

// Función para actualizar el localStorage con el contenido del carrito
function actualizarLocalStorage() {
  const listaCarrito = document.getElementById("lista-carrito");
  const items = listaCarrito.querySelectorAll("li");
  const carrito = Array.from(items).map(item => {
    const [nombre, precioTexto] = item.querySelector("span").textContent.split(" - $");
    return { nombre, precio: parseFloat(precioTexto) };
  });

  localStorage.setItem('carrito', JSON.stringify(carrito));
  console.log('Carrito guardado en localStorage:', carrito);
}

// Función para cargar el carrito desde localStorage al iniciar la página
function cargarCarritoDesdeLocalStorage() {
  const carritoGuardado = localStorage.getItem('carrito');
  if (carritoGuardado) {
    const carrito = JSON.parse(carritoGuardado);
    const listaCarrito = document.getElementById("lista-carrito");

    carrito.forEach(producto => {
      const item = document.createElement("li");

      const texto = document.createElement("span");
      texto.textContent = producto.nombre + " - $" + producto.precio.toFixed(1);

      const eliminar = document.createElement("button");
      eliminar.textContent = "Eliminar";
      eliminar.classList.add("boton-eliminar");
      eliminar.addEventListener("click", function() {
        eliminarProductoDelCarrito(item, producto.precio);
      });

      item.appendChild(texto);
      item.appendChild(eliminar);
      listaCarrito.appendChild(item);

      actualizarTotal(producto.precio);
    });

    // Actualizar el contenido del off-canvas
    actualizarOffCanvas();
    console.log('Carrito cargado desde localStorage:', carrito);
  }
}