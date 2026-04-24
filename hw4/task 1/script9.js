const input = document.getElementById("input");
const text = document.getElementById("text");

input.addEventListener("input", () => {
    text.textContent = "Вы ввели: " + input.value;
});
