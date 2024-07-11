document.addEventListener("DOMContentLoaded", function () {
    const productsContainer = document.getElementById('products-container');
  
    // Funcion para cortare el texto y no sea largo
    function truncateText(text, maxLength) {
      return text.length > maxLength ? text.substring(0, 25) + "..." : text;
    }
  
    // Obtener todos los productos
    function fetchProducts() {
      fetch('https://comerciando.pythonanywhere.com/productos')
        .then(response => response.json())
        .then(data => {
          data.forEach(product => {
            const productCard = document.createElement('div');
            productCard.className = 'product-card';
  
            productCard.innerHTML = `
              <div class="product-img">
                <img src="${product.imagen}" alt="${product.nombre}">
                ${product.promo ? `<div class="promo">${product.promo}</div>` : ''}
              </div>
              <div class="product-info">
                <h3>${truncateText(product.nombre, 25)}</h3>
                <strong>$ ${product.precio}</strong>
                <a href="#" class="add-cart">Añadir al carrito</a>
              </div>
            `;
  
            productsContainer.appendChild(productCard);
          });
        })
        .catch(error => console.error('Error fetching products:', error));
    }
  
    fetchProducts();
  });