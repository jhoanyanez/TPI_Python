document.addEventListener('DOMContentLoaded', function() {
    const logoutButton = document.querySelector('.logout-button');
    
    logoutButton.addEventListener('click', function() {
      // Aquí puedes agregar la lógica para cerrar sesión
      alert('Cerrando sesión...');
      // Redirigir a la página de login
      window.location.href = 'login.html';
    });
  });