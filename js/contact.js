document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
  
    form.addEventListener('submit', function (event) {
      event.preventDefault();
  
      const nombre = document.querySelector('input[name="nombre"]');
      const email = document.querySelector('input[name="email"]');
      const mensaje = document.querySelector('textarea[name="mensaje"]');
      const errorMessageNombre = document.querySelector('input[name="nombre"] + .error-message');
      const errorMessageEmail = document.querySelector('input[name="email"] + .error-message');
      const errorMessageMensaje = document.querySelector('textarea[name="mensaje"] + .error-message');
  
      // Validación de nombre
      if (nombre.value.trim() === '') {
        errorMessageNombre.textContent = 'Por favor, ingrese su nombre.';
        return;
      } else {
        errorMessageNombre.textContent = '';
      }
  
      // Validación de email
      if (email.value.trim() === '') {
        errorMessageEmail.textContent = 'Por favor, ingrese su correo electrónico.';
        return;
      } else {
        errorMessageEmail.textContent = '';
      }
  
      // Validación de mensaje
      if (mensaje.value.trim() === '') {
        errorMessageMensaje.textContent = 'Por favor, ingrese su mensaje.';
        return;
      } else {
        errorMessageMensaje.textContent = '';
      }
  
      // Limpiar el formulario
      form.reset();
  
      // Mostrar un alert de forma ficticia simulando el envío de formulario,mas adelante implementaremos otra funcion.
      alert('Mensaje enviado');
    });
  });