function toggleContent() {
  const extra = document.getElementById("extraContent");
  if (extra.style.display === "block") {
    extra.style.display = "none";
  } else {
    extra.style.display = "block";
  }
}

document.addEventListener("DOMContentLoaded", function() {
  const images = document.querySelectorAll(".images img");
  images.forEach(image => {
    image.addEventListener("mouseover", function() {
      image.style.transition = "transform 0.3s ease";
      image.style.transform = "scale(1.2)";
    });
    image.addEventListener("mouseout", function() {
      image.style.transform = "scale(1)";
    });
  });

  const waterBtn = document.querySelector(".water-btn");
  waterBtn.addEventListener("click", function(e) {
    
    waterBtn.classList.add("ripple");

    setTimeout(() => {
      waterBtn.classList.remove("ripple");
    }, 600);
  });
});
