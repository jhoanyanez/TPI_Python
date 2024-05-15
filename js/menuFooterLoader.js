document.addEventListener("DOMContentLoaded", function() {
    // Cargar el contenido del menú desde menu.html
    fetch('menu.html')
      .then(response => response.text())
      .then(data => {
        document.getElementById('menu-container').innerHTML = data;
      });
  
    // Cargar el contenido del pie de página desde footer.html
    fetch('footer.html')
      .then(response => response.text())
      .then(data => {
        document.getElementById('footer-container').innerHTML = data;
      });
  });