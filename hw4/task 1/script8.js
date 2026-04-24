const box = document.getElementById("box");
const btn = document.getElementById("btn");

box.onmouseover = () => {
    box.style.background = "yellow";
};

box.onmouseout = () => {
    box.style.background = "white";
};

btn.onclick = () => {
    alert("Кнопка нажата");
};
