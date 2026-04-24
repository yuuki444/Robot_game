const title = document.getElementById("title");
const btn = document.getElementById("btn");
const box = document.getElementById("box");

btn.onclick = () => {
    title.textContent = "DOM работает!";
    box.innerHTML = "<b>Это жирный текст</b>";
};
