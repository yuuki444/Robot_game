let count = 0;
const countEl = document.getElementById("count");
const plus = document.getElementById("plus");
const minus = document.getElementById("minus");

plus.onclick = () => {
    count++;
    countEl.textContent = count;
};

minus.onclick = () => {
    count--;
    countEl.textContent = count;
};
