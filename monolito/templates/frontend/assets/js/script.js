/* Archivo: script.js */

// Función para mostrar la sección seleccionada y ocultar las demás
function mostrarSeccion(id) {
    const secciones = document.querySelectorAll('.seccion');
    secciones.forEach(seccion => seccion.style.display = 'none');
    document.getElementById(id).style.display = 'block';
}

// Función para agregar un producto a la lista de productos
function agregarProducto() {
    const nombre = document.getElementById('nombreProducto').value;
    const tipo = document.getElementById('tipoProducto').value;
    const stock = document.getElementById('stockProducto').value;
    const precio = document.getElementById('precioProducto').value;

    if (nombre && tipo && stock && precio) {
        const tabla = document.getElementById('tablaProductos');
        const fila = document.createElement('tr');
        fila.innerHTML = `
            <td>${nombre}</td>
            <td>${tipo}</td>
            <td>${stock}</td>
            <td>${precio}</td>
        `;
        tabla.appendChild(fila);
        document.getElementById('formProducto').reset();
        alert('Producto agregado con éxito');
    } else {
        alert('Por favor complete todos los campos para agregar un producto.');
    }
}
