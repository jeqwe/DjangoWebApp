let btn = document.getElementById("send-news");

btn.addEventListener("click", active);

function active() {
  btn.classList.toggle("is_active");
}