const modalBtns = document.querySelectorAll('.ver-vehiculo-btn');
    const modal = document.getElementById('myModal');
    const closeBtn = modal.querySelector('.close');

    // Función para mostrar el modal
    function openModal() {
        modal.style.display = 'block';
    }

    // Función para cerrar el modal
    function closeModal() {
        modal.style.display = 'none';
    }

    // Asignar el evento de clic a los botones
    modalBtns.forEach(btn => {
        btn.addEventListener('click', openModal);
    });

    // Asignar el evento de clic al botón de cerrar
    closeBtn.addEventListener('click', closeModal);

    // Cerrar el modal si el usuario hace clic fuera del contenido del modal
    window.addEventListener('click', (event) => {
        if (event.target === modal) {
            closeModal();
        }
    });

const slider = document.querySelector('.slider');
const slides = slider.querySelectorAll('.slide');
let slideIndex = 0;

function updateSliderPosition() {
  slider.style.transform = `translateX(-${slideIndex * 100}%)`;
}

// Desplazamiento automático del slider cada 3 segundos (puedes ajustar el tiempo según tus necesidades)
setInterval(() => {
  slideIndex = (slideIndex + 1) % slides.length;
  updateSliderPosition();
}, 3000);

document.addEventListener("DOMContentLoaded", function() {
  var submitBtn = document.querySelector(".submit-btn");
  var form = document.querySelector(".contact-form");

  form.addEventListener("input", function() {
    var name = form.querySelector("input[name='name']");
    var email = form.querySelector("input[name='email']");
    var message = form.querySelector("textarea[name='message']");
    
    if (name.value !== "" && email.value !== "" && message.value !== "") {
      submitBtn.classList.add("valid");
    } else {
      submitBtn.classList.remove("valid");
    }
  });
});

window.sr = ScrollReveal();
  sr.reveal('.container',{
    duration: 300, 
    origin: 'left',
    distance: '300px'
  })

  sr.reveal('.benefit',{
    duration: 1900, 
    origin: 'bottom',
    distance: '300px'
  })

1 