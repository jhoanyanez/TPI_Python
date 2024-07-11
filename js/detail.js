document.addEventListener('DOMContentLoaded', function () {
  const productDetailContainer = document.getElementById('product-detail-container');

  // obtener el ID del producto
  function getProductIdFromUrl() {
      const params = new URLSearchParams(window.location.search);
      return params.get('id');
  }

  // btener los detalles del producto
  function fetchProductDetails(productId) {
      fetch(`https://comerciando.pythonanywhere.com/productos/${productId}`)
          .then((response) => response.json())
          .then((product) => {
              const productDetailHTML = `
                  <div class="product-img">
                      <img src="${product.imagen}" alt="${product.nombre}">
                  </div>
                  <div class="product-info">
                      <h1>${product.nombre}</h1>
                      <p><strong>Precio:</strong> $${product.precio}</p>
                      <p class="description"><strong>Descripción:</strong> ${product.descripcion}</p>
                      <a href="#" class="add-cart">Añadir al carrito</a>
                  </div>
              `;
              productDetailContainer.innerHTML = productDetailHTML;
          })
          .catch((error) => console.error('Error fetching product details:', error));
  }

  // Obtener el id del producto y obtener los detalles del producto
  const productId = getProductIdFromUrl();
  if (productId) {
      fetchProductDetails(productId);
  } else {
      productDetailContainer.innerHTML = '<p>Producto no encontrado.</p>';
  }
});