const title = document.getElementById("title");
const texts = document.querySelectorAll(".text");
const btn = document.getElementById("btn");

btn.onclick = () => {
    title.style.color = "white";
    title.style.fontSize = "50px";
    title.style.backgroundColor = "black";

    texts.forEach(p => {
        p.style.color = "blue";
        p.style.fontSize = "20px";
    });
};
