// Script Banner Slider

let slideIndex = 1;
showSlides(slideIndex);

function moveSlide(n) {
  showSlides(slideIndex += n);
}

function showSlides(n) {
  const slides = document.querySelectorAll('.slider img');
  
  if (n > slides.length) {
    slideIndex = 1;
  }    
  if (n < 1) {
    slideIndex = slides.length;
  }
  
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none';  
  }
  
  slides[slideIndex - 1].style.display = 'block';  
}

// Desplazamiento automático
setInterval(() => {
  moveSlide(1);
}, 3000); // Cambiar la imagen cada 3 segundos


// Obtener los últimos 10 productos  y actualizar la sección de productos
fetch('https://comerciando.pythonanywhere.com/productos')
    .then(response => response.json())
    .then(data => {
      const productContainer = document.querySelector('.products-container');
      data.slice(-10).forEach(product => {
        const productCard = document.createElement('div');
        productCard.classList.add('product-card');
        productCard.innerHTML = `
          <a href="./detail.html?id=${product.id_producto}">
            <div class="product-img">
              <img src="${product.imagen}" alt="${product.nombre}">
              <span class="promo">Nuevo ingreso</span>
            </div>
          </a>
          <div class="product-info">
            <h3>${product.nombre}</h3>
            <strong>$ ${product.precio}</strong>
            <span class="rating">★★★★☆</span>
            <a href="#" class="add-cart">Añadir al carrito</a>
          </div>
        `;
        productContainer.appendChild(productCard);
      });
    })
    .catch(error => console.error('Error fetching products:', error));