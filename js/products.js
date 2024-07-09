document.addEventListener('DOMContentLoaded', function () {
    const createProductBtn = document.getElementById('create-product-btn');
    const modal = document.getElementById('create-product-modal');
    const closeModalBtn = document.querySelector('.modal .close');
    const createProductForm = document.getElementById('create-product-form');
    const tableBody = document.querySelector('#products-table tbody');
    const categoriasSelect = document.getElementById('categorias');

    function fetchProducts() {
        fetch('https://comerciando.pythonanywhere.com/productos')
            .then(response => response.json())
            .then(data => {
                tableBody.innerHTML = '';
                data.forEach(product => {
                    const row = document.createElement('tr');
                    const categories = product.categorias.map(cat => cat.nombre).join(', ');
                    row.innerHTML = `
                        <td>${product.id_producto}</td>
                        <td>${product.nombre}</td>
                        <td class="description">${product.descripcion}</td>
                        <td>$ ${product.precio}</td>
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
    }

    function fetchCategorias() {
        fetch('https://comerciando.pythonanywhere.com/categorias')
            .then(response => response.json())
            .then(data => {
                categoriasSelect.innerHTML = '';
                data.forEach(categoria => {
                    const option = document.createElement('option');
                    option.value = categoria.id_categoria;
                    option.textContent = categoria.nombre;
                    categoriasSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error fetching categories:', error));
    }

    createProductBtn.addEventListener('click', function () {
        modal.style.display = 'block';
        fetchCategorias(); // Cargar categorías cuando se abre el modal
    });

    closeModalBtn.addEventListener('click', function () {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });

    createProductForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(createProductForm);
        const productData = {};
        formData.forEach((value, key) => {
            if (key === 'categorias') {
                if (!productData[key]) {
                    productData[key] = [];
                }
                productData[key].push(value);
            } else {
                productData[key] = value;
            }
        });

        fetch('https://comerciando.pythonanywhere.com/productos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(productData)
        })
            .then(response => response.json())
            .then(data => {
                // Cerrar el modal
                modal.style.display = 'none';
                // Resetear el formulario
                createProductForm.reset();
                // Actualizar la tabla con los nuevos datos
                fetchProducts();
            })
            .catch(error => console.error('Error creating product:', error));
    });

    fetchProducts();
});