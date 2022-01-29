let h1 = document.querySelector("h1");
let body = document.querySelector("body");
let inputs = document.querySelectorAll(".boxes");
let div = document.querySelector("div");

function randomColor() {
  let r = Math.floor(Math.random() * 256);
  let g = Math.floor(Math.random() * 256);
  let b = Math.floor(Math.random() * 256);

  return `rgb(${r},${g},${b})`;
}

h1.addEventListener("click", function (e) {
  body.style.backgroundColor = randomColor();
});

const intervalId = setInterval(function () {
  for (let input of inputs) {
    input.style.backgroundColor = randomColor();
  }

  h1.style.backgroundColor = randomColor();
}, 1000);
