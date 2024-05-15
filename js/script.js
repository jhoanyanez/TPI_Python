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


