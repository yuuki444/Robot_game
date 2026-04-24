const input = document.getElementById("name");
const btn = document.getElementById("btn");
const result = document.getElementById("result");

btn.onclick = () => {
    const name = input.value.trim();

    if (name === "") {
        result.textContent = "Введите имя";
        return;
    }

    result.textContent = `Привет, ${name}!`;
};
