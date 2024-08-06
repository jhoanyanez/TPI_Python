document.addEventListener('DOMContentLoaded', function() {
    const integrantesContainer = document.getElementById('integrantes-container');

    // Cargar integrantes desde json
    function cargarIntegrantes() {
        fetch('data/integrantes.json')
            .then(response => response.json())
            .then(data => {
                data.forEach(integrante => {
                    const integranteHTML = `
                        <div class="col-xl-4 col-sm-6 col-md-6 col-lg-4">
                            <div class="card rounded-lg shadow p-4 p-xl-5 mb-4 text-center">
                                <div class="banner rounded-top"></div>
                                <img src="img/user/${integrante.foto}" alt="" class="img-circle mx-auto mb-3">
                                <h5 class="mb-1">${integrante.nombre}</h5>
                                <p class="mb-4">${integrante.rol}</p>
                                <div class="social-links d-flex justify-content-center">
                                    <a href="https://github.com/${integrante.github}" class="mx-2" target="_blank"><img src="img/social/github.svg" alt="Github"></a>
                                    <a href="https://linkedin.com/in/${integrante.linkedin}" class="mx-2" target="_blank"><img src="img/social/linkedin.svg" alt="Linkedin"></a>
                                </div>
                            </div>
                        </div>
                    `;
                    integrantesContainer.innerHTML += integranteHTML;
                });
            })
            .catch(error => console.error('Error cargando integrantes:', error));
    }

    cargarIntegrantes();
});