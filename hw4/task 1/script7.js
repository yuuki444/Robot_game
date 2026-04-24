const input = document.getElementById("password");
const btn = document.getElementById("toggle");

btn.onclick = () => {
    if (input.type === "password") {
        input.type = "text";
        btn.textContent = "hide";
    } else {
        input.type = "password";
        btn.textContent = "show";
    }
};
