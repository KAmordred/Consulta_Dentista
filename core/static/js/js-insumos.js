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

  // Ajustar la altura del contenedor de carrito dinámicamente
  ajustarAlturaContenedorCarrito();
}

// Función para eliminar un producto del carrito
function eliminarProductoDelCarrito(item, precioProducto) {
  item.remove();
  actualizarTotal(-precioProducto);
  actualizarLocalStorage(); // Actualizar el localStorage al eliminar

  // Actualizar el contenido del off-canvas
  actualizarOffCanvas();

  // Ajustar la altura del contenedor de carrito dinámicamente
  ajustarAlturaContenedorCarrito();
}

// Función para ajustar dinámicamente la altura del contenedor de carrito
function ajustarAlturaContenedorCarrito() {
  const contenedorCarrito = document.querySelector(".contenedor-carrito");
  const listaCarrito = document.getElementById("lista-carrito");
  const total = document.getElementById("total");

  // Calcular la altura mínima necesaria para mostrar todo el contenido
  const alturaMinima = listaCarrito.offsetHeight + total.offsetHeight + 40; // 40px de margen adicional

  // Ajustar la altura mínima del contenedor
  contenedorCarrito.style.minHeight = alturaMinima + "px";
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

    // Ajustar la altura del contenedor de carrito después de cargar
    ajustarAlturaContenedorCarrito();
  }
}

// Cargar el carrito desde localStorage al iniciar la página
cargarCarritoDesdeLocalStorage();
