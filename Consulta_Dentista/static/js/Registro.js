function validarFormulario() {
    var password = document.getElementById("pass").value;
    var confirmPassword = document.getElementById("confirmPass").value;
    var MensajePantalla = document.querySelector('#exampleModal .modal-body');

    if (password !== confirmPassword) {
        MensajePantalla.innerHTML = '<p style="color: red;">Las contraseñas no coinciden</p>';
        return false; 
    }

    // AVISO PARA EL REGISTRO
    var mensaje = "¡Registro exitoso!"; 

    // SE MOSTRARÁ EN EL MODAL EL MENSAJE DE REGISTRO 
    MensajePantalla.innerHTML = '<p>' + mensaje + '</p>';

    return true; // Permitir el envío del formulario si las contraseñas coinciden
}


document.addEventListener("DOMContentLoaded", function() {
    
    var form = document.querySelector('#exampleModal form');

    
    form.addEventListener('submit', function(event) {
       
        if (!validarFormulario()) {
            event.preventDefault();
        }
    });
});
