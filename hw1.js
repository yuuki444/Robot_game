// 1
let a = Number(prompt("Введите число"));
let sum = 0;
let i = 1;

while (i <= a) {
    sum += i;
    i++;
}

console.log(sum);


// 2
let num = 1234;
let reversed = 0;

while (num > 0) {
    let j = num % 10;
    reversed = reversed * 10 + j; 
    num = (num - j) / 10;
}

console.log(reversed);

// 3
let secret = 7; 
let guess;

do {
    guess = prompt("число от 1 до 10");
} while (guess != secret);

alert("получилось");
// 4
const password = "12345";
let attempts = 3;
let input;

do {
    input = prompt("Введите пароль:");
    attempts--;

    if (input === password) {
        alert("Доступ разрешён");
        break;
    }

    if (attempts > 0) {
        alert("Осталось " + attempts);
    }

} while (attempts > 0);

if (input !== password) {
    alert("Доступ заблокирован");
}


// 5
let b = Number(prompt("Введите число для чётных чисел:"));

for (let i = 1; i <= b; i++) {
    if (i % 2 === 0) {
        console.log(i);
    }
}


// 6
let c = Number(prompt("Введите число для факториала:"));
let factorial = 1;

for (let i = 1; i <=c; i++) {
    factorial *= i;
}

console.log(factorial);
