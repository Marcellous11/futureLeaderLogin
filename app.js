let h1 = document.querySelector("h1");
let body = document.querySelector("body");

function randomColor() {
  let r = Math.floor(Math.random() * 256);
  let g = Math.floor(Math.random() * 256);
  let b = Math.floor(Math.random() * 256);

  return `rgb(${r},${g},${b})`;
}

h1.addEventListener("click", function (e) {
  console.log(e.target);
  body.style.backgroundColor = randomColor();
});
