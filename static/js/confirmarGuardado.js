function enviarFormulario(e, mensaje){
    e.preventDefault();

    Swal.fire({
        title : 'Confirmación',
        text: mensaje,
        cancelButtonText: 'Cancelar',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText : 'Aceptar'
    }).then((resultado) => {
        if(resultado.isConfirmed){
            const formulario = document.getElementById('formulario');
            formulario.submit()
        }
    })
}
