let carrito = [];
let recargoEnvio = 0;

// Función para mostrar u ocultar el offcanvas del carrito
function toggleCartOffcanvas() {
    var offcanvasElement = document.getElementById('cartOffcanvas');
    var offcanvas = new bootstrap.Offcanvas(offcanvasElement);
    offcanvas.toggle();
    actualizarCarritoOffcanvas();
}

// Función para agregar producto al carrito
function agregarProductoAlCarrito(nombre, precio, imagen_url, stock) {
    // Buscar si el producto ya está en el carrito
    let encontrado = false;
    carrito.forEach((producto) => {
        if (producto.nombre === nombre) {
            producto.cantidad++;
            encontrado = true;
        }
    });
    // Si el producto no está en el carrito, agregarlo
    if (!encontrado) {
        carrito.push({ nombre: nombre, precio: precio, cantidad: 1, imagen_url: imagen_url, stock: stock });
    }
    actualizarCarrito();
    guardarCarritoEnLocalStorage();
    actualizarCarritoOffcanvas();
}

// Función para actualizar el carrito y calcular el subtotal, iva y total
function actualizarCarrito() {
    const listaCarrito = document.getElementById('lista-carrito');
    let subtotal = 0;
    listaCarrito.innerHTML = '';
    carrito.forEach((producto) => {
        const item = document.createElement('li');
        item.textContent = `${producto.cantidad} x ${producto.nombre} - $${producto.precio * producto.cantidad}`;
        const botonEliminar = document.createElement('button');
        botonEliminar.textContent = 'Eliminar';
        botonEliminar.classList.add('boton-eliminar');
        botonEliminar.onclick = () => eliminarProductoDelCarrito(producto);
        item.appendChild(botonEliminar);
        listaCarrito.appendChild(item);
        subtotal += producto.precio * producto.cantidad;
    });
    const iva = subtotal * 0.19;
    const total = subtotal + iva + recargoEnvio;
    document.getElementById('subtotal').textContent = `Sub Total: $${subtotal.toFixed(2)}`;
    document.getElementById('iva').textContent = `IVA 19%: $${iva.toFixed(2)}`;
    document.getElementById('total').textContent = `Monto a pagar: $${total.toFixed(2)}`;
}

// Función para eliminar un producto del carrito
function eliminarProductoDelCarrito(producto) {
    const index = carrito.indexOf(producto);
    if (index !== -1) {
        carrito.splice(index, 1);
        actualizarCarrito();
        guardarCarritoEnLocalStorage();
        actualizarCarritoOffcanvas();
    }
}

// Función para simular el pago (ejemplo)
function simularPago() {
    alert('Pago realizado con éxito');
    vaciarCarrito();
}

// Función para guardar el carrito en localStorage
function guardarCarritoEnLocalStorage() {
    localStorage.setItem('carrito', JSON.stringify(carrito));
}

// Función para cargar el carrito desde localStorage al cargar la página
function cargarCarritoDesdeLocalStorage() {
    const carritoGuardado = localStorage.getItem('carrito');
    if (carritoGuardado) {
        carrito = JSON.parse(carritoGuardado);
        actualizarCarrito();
    }
}

// Función para vaciar el carrito
function vaciarCarrito() {
    carrito = [];
    actualizarCarrito();
    localStorage.removeItem('carrito');
    actualizarCarritoOffcanvas();
}

// Función para actualizar el carrito en el offcanvas
function actualizarCarritoOffcanvas() {
    const cartItemsList = document.getElementById('cart-items');
    cartItemsList.innerHTML = '';
    let subtotal = 0;
    carrito.forEach(producto => {
        const cartItem = document.createElement('li');
        cartItem.textContent = `${producto.cantidad} x ${producto.nombre} - $${producto.precio * producto.cantidad}`;
        cartItemsList.appendChild(cartItem);
        subtotal += producto.precio * producto.cantidad;
    });

    const iva = subtotal * 0.19;
    const total = subtotal + iva + recargoEnvio;

    document.getElementById('cart-subtotal').textContent = `Sub Total: $${subtotal.toFixed(2)}`;
    document.getElementById('cart-iva').textContent = `IVA (19%): $${iva.toFixed(2)}`;
    document.getElementById('cart-total').textContent = `Monto a pagar: $${total.toFixed(2)}`;
}

// Función para actualizar el total a pagar basado en la opción de envío
function actualizarTotalConEnvio() {
    const envio = document.querySelector('input[name="envio"]:checked').value;
    recargoEnvio = (envio === 'despacho') ? 4500 : 0;
    actualizarCarritoOffcanvas();
}

// Evento que se ejecuta al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    cargarCarritoDesdeLocalStorage();
    actualizarCarritoOffcanvas(); // Actualiza el carrito en el offcanvas al cargar la página
    document.getElementById('retiroTienda').addEventListener('change', actualizarTotalConEnvio);
    document.getElementById('despachoDomicilio').addEventListener('change', actualizarTotalConEnvio);
});

// Evento que se ejecuta al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    cargarCarritoDesdeLocalStorage();
    actualizarCarritoOffcanvas(); // Asegura que el offcanvas del carrito se actualice en cada página
});