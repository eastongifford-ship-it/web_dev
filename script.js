
function toggleContent() {
  const extra = document.getElementById("extraContent");
  if (extra.style.display === "none" || extra.style.display === "") {
    extra.style.display = "block";
  } else {
    extra.style.display = "none";
  }
}


document.addEventListener("DOMContentLoaded", () => {
  const hoverImage = document.querySelector(".images img"); 
  hoverImage.addEventListener("mouseover", () => {
    hoverImage.style.transform = "scale(1.2)";
    hoverImage.style.transition = "transform 0.3s ease";
  });
  hoverImage.addEventListener("mouseout", () => {
    hoverImage.style.transform = "scale(1)";
  });
});
