document.addEventListener('DOMContentLoaded', function() {
var menuContainer = document.getElementById('menu');

var menuURL = '../dashboard/menu-dashboard.html';

    fetch(menuURL)
        .then(response => response.text())
        .then(data => {
            menuContainer.innerHTML = data;
        })
        .catch(error => console.error('Error al cargar el menú:', error));
});