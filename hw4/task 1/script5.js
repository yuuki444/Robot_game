const message = document.getElementById("message");
const btn = document.getElementById("btn");

btn.onclick = () => {
    message.classList.toggle("dark");
};
