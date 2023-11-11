



setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000)


function leftScroll() {
  const left = document.querySelector(".scroll-imagesCat");
  left.scrollBy(200, 0);
}
function rightScroll() {
  const right = document.querySelector(".scroll-imagesCat");
  right.scrollBy(-200, 0);
}

function leftScrollM() {
  const left = document.querySelector(".scroll-imagesMethod");
  left.scrollBy(200, 0);
}
function rightScrollM() {
  const right = document.querySelector(".scroll-imagesMethod");
  right.scrollBy(-200, 0);
}
