document.addEventListener('DOMContentLoaded', function () {
    fetch('http://127.0.0.1:5000/productos')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#products-table tbody');
            if (!tableBody) {
                console.error('No se encontró el tbody en la tabla #products-table');
                return;
            }
            data.forEach(product => {
                const row = document.createElement('tr');
                const categories = product.categorias.map(cat => cat.nombre).join(', ');
                row.innerHTML = `
                    <td>${product.id_producto}</td>
                    <td>${product.nombre}</td>
                    <td class="description">${product.descripcion}</td>
                    <td>${product.precio}</td>
                    <td>${product.cantidad}</td>
                    <td><img src="${product.imagen}" alt="${product.nombre}" style="width:50px; height:auto;"></td>
                    <td>${categories}</td>
                    <td>
                        <button class="edit-btn" data-id="${product.id_producto}">Editar</button>
                        <button class="delete-btn" data-id="${product.id_producto}">Borrar</button>
                    </td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching products:', error));
});