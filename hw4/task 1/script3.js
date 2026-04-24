const img = document.getElementById("img");
const link = document.getElementById("link");
const btn = document.getElementById("btn");

btn.onclick = () => {
    img.src = "";
    img.alt = "новое изображение";

    link.href = "";
    link.textContent = "ссылка";
};
