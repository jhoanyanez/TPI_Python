document.addEventListener("DOMContentLoaded", function() {
    // Cargar el contenido del menú desde menu.html
    fetch('top-menu.html')
      .then(response => response.text())
      .then(data => {
        document.getElementById('menu-container').innerHTML = data;
      });

  });