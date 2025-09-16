function agregarCarrito(e, form) {
    e.preventDefault(); // evita que recargue la página

    $.ajax({
        type: "POST",
        url: $(form).attr("action"), // la URL del action del form
        data: $(form).serialize(),   // serializa datos del form
        success: function (response) {
            Swal.fire({
                icon: "success",
                title: "Producto agregado",
                text: "El producto se añadió correctamente al carrito",
                timer: 3000,
                showConfirmButton: true,
                confirmButtonText : 'Aceptar'
            });
        },
        error: function (xhr) {
            Swal.fire({
                icon: "error",
                title: "Error",
                text: "Debe iniciar sesión para agregar productos al carrito",
                timer: 3000,
                showConfirmButton: true,
                confirmButtonText : 'Aceptar'
            });
        }
    });
}