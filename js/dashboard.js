document.addEventListener('DOMContentLoaded', function() {
  const links = document.querySelectorAll('.sidebar a');
  const content = document.querySelector('.content');

  // Cargar statistics.html al inicio del dashboard
  loadSectionContent('statistics');

  links.forEach(link => {
      link.addEventListener('click', function(event) {
          event.preventDefault();
          const sectionId = this.getAttribute('data-section');
          loadSectionContent(sectionId);
      });
  });

  function loadSectionContent(sectionId) {
      fetch(`${sectionId}.html`)
          .then(response => response.text())
          .then(data => {
              content.innerHTML = data;
          })
          .catch(error => {
              console.error('Error al cargar el contenido:', error);
              content.innerHTML = `<p>Error al cargar el contenido de la sección ${sectionId}</p>`;
          });
  }
});