let h1 = document.querySelector("h1");
let body = document.querySelector("body");
let inputs = document.querySelectorAll(".boxes");
let div = document.querySelector("div");

function randomColor() {
  let r = Math.floor(Math.random() * 256);
  let g = Math.floor(Math.random() * 150);
  let b = Math.floor(Math.random() * 150);

  return `rgb(0,${g},${b})`;
}

const intervalId = setInterval(function () {
  for (let input of inputs) {
    input.style.backgroundColor = randomColor();
  }
}, 1000);
