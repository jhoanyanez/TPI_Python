document.addEventListener('DOMContentLoaded', function () {
    const createProductBtn = document.getElementById('create-product-btn');
    const modal = document.getElementById('create-product-modal');
    const editModal = document.getElementById('edit-product-modal');
    const closeModalBtns = document.querySelectorAll('.modal .close');
    const createProductForm = document.getElementById('create-product-form');
    const editProductForm = document.getElementById('edit-product-form');
    const tableBody = document.querySelector('#products-table tbody');
    const categoriasSelect = document.getElementById('categorias');
    const editCategoriasSelect = document.getElementById('edit-categorias');

    // Función para obtener la lista de productos
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
                            <button class="delete-btn" data-id="${product.id_producto}">Eliminar</button>
                        </td>
                    `;
                    tableBody.appendChild(row);
                });

                // evento de los botones editar y eliminar botones
                document.querySelectorAll('.edit-btn').forEach(button => {
                    button.addEventListener('click', function () {
                        const productId = button.getAttribute('data-id');
                        openEditModal(productId);
                    });
                });

                document.querySelectorAll('.delete-btn').forEach(button => {
                    button.addEventListener('click', function () {
                        const productId = button.getAttribute('data-id');
                        deleteProduct(productId);
                    });
                });
            })
            .catch(error => console.error('Error fetching products:', error));
    }

    // Función para obtener las categorías y llenar el select
    function fetchCategorias(selectElement) {
        fetch('https://comerciando.pythonanywhere.com/categorias')
            .then(response => response.json())
            .then(data => {
                selectElement.innerHTML = '';
                data.forEach(categoria => {
                    const option = document.createElement('option');
                    option.value = categoria.id_categoria;
                    option.textContent = categoria.nombre;
                    selectElement.appendChild(option);
                });
            })
            .catch(error => console.error('Error fetching categories:', error));
    }

    // Función para abrir el modal de edición y llenar los datos del producto
function openEditModal(productId) {
    fetch(`https://comerciando.pythonanywhere.com/productos/${productId}`)
        .then(response => response.json())
        .then(product => {
            document.getElementById('edit-nombre').value = product.nombre;
            document.getElementById('edit-descripcion').value = product.descripcion;
            document.getElementById('edit-precio').value = product.precio;
            document.getElementById('edit-cantidad').value = product.cantidad;
            document.getElementById('edit-imagen').value = product.imagen;

            // Cargar las categorías y seleccionar la categorías del producto
            fetchCategorias(editCategoriasSelect);
            setTimeout(() => {
                product.categorias.forEach(cat => {
                    const option = Array.from(editCategoriasSelect.options).find(opt => opt.value == cat.id_categoria);
                    if (option) option.selected = true;
                });
            }, 500);

            editModal.style.display = 'block';

            editProductForm.onsubmit = function (event) {
                event.preventDefault();
                const formData = new FormData(editProductForm);
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

                fetch(`https://comerciando.pythonanywhere.com/productos/${productId}`, {
                    method: 'PUT',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(productData)
                })
                    .then(response => response.json())
                    .then(data => {
                        editModal.style.display = 'none';
                        fetchProducts();
                    })
                    .catch(error => console.error('Error updating product:', error));
            };
        })
        .catch(error => console.error('Error fetching product:', error));
}

    // Función para eliminar un producto por su ID
    function deleteProduct(productId) {
        fetch(`https://comerciando.pythonanywhere.com/productos/${productId}`, {
            method: 'DELETE'
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => { throw new Error(err.message) });
            }
            return response.json();
        })
        .then(data => {
            fetchProducts();
        })
        .catch(error => console.error('Error deleting product:', error));
    }

    // Abrir el modal de creación de producto
    createProductBtn.addEventListener('click', function () {
        modal.style.display = 'block';
        fetchCategorias(categoriasSelect);
    });

    // cerrar los modales al hacer clic en el botón de cerrar
    closeModalBtns.forEach(btn => {
        btn.addEventListener('click', function () {
            modal.style.display = 'none';
            editModal.style.display = 'none';
        });
    });

    // cerar los modales al hacer clic fuera del modal
    window.addEventListener('click', function (event) {
        if (event.target === modal || event.target === editModal) {
            modal.style.display = 'none';
            editModal.style.display = 'none';
        }
    });

    // enviar el formulario de creación de producto
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
                modal.style.display = 'none';
                createProductForm.reset();
                fetchProducts();
            })
            .catch(error => console.error('Error creating product:', error));
    });

    editProductForm.querySelector('.btn-cancel').addEventListener('click', function () {
        editModal.style.display = 'none';
        editProductForm.reset();
    });

    // Cargar y mostrar los productos al cargar la página
    fetchProducts();
});