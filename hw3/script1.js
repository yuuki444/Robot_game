const nameInput = document.getElementById("nameInput");
const sendBtn = document.getElementById("sendBtn");
const result = document.getElementById("result");
const error = document.getElementById("error");

sendBtn.addEventListener("click", () => {
    const name = nameInput.value.trim();

    error.textContent = "";
    result.textContent = "";

    if (name === "") {
        error.textContent = "Введите имя";
        return;
    }

    if (name.length < 2) {
        error.textContent = "Имя слишком короткое";
        return;
    }

    result.textContent = `Здравствуйте, ${name}!`;

    nameInput.value = "";
});
