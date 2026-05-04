//1
btn1.onclick = () => title1.textContent = "Новый заголовок"

//2
btn2.onclick = () => text2.style.color = "red"

//3
btn3.onclick = () => {
box3.style.backgroundColor = "blue"
box3.style.color = "white"
box3.style.padding = "20px"
}

//4
btn4.onclick = function() {
this.textContent = "Нажато"
this.style.background = "green"
this.style.color = "white"
this.style.padding = "15px"
}

//5
btn5.onclick = () => {
result5.textContent = "Привет, " + nameInput5.value
}

//6
form6.onsubmit = e => {
e.preventDefault()
result6.textContent = "Ваш email: " + emailInput6.value
}

//7
form7.onsubmit = e => {
e.preventDefault()
if (nameInput7.value === "") {
message7.textContent = "Введите имя"
} else {
message7.textContent = "Привет, " + nameInput7.value
}
}

//8
btn8.onclick = () => image8.src = ""

//9
hideBtn9.onclick = () => text9.style.display = "none"
showBtn9.onclick = () => text9.style.display = "block"

//10
btn10.onclick = () => {
name10.textContent = "Dias"
age10.textContent = "21"
name10.style.color = "blue"
age10.style.fontSize = "20px"
}

//11
function getData() {
return new Promise(r => setTimeout(() => r("Данные успешно загружены"),2000))
}
btn11.onclick = async () => {
result11.textContent = "Загрузка..."
result11.textContent = await getData()
}

//12
function getUser() {
return new Promise(r => setTimeout(() => r({name:"Aruzhan",age:19}),1000))
}
btn12.onclick = async () => {
let u = await getUser()
result12.textContent = `Пользователь: ${u.name}, возраст: ${u.age}`
}

//13
form13.onsubmit = e => {
e.preventDefault()
message13.textContent =
passwordInput13.value.length < 6
? "Пароль слишком короткий"
: "Пароль подходит"
}

//14
btn14.onclick = () => {
title14.textContent = "Мой первый DOM сайт"
description14.textContent = "Я научился менять HTML через JavaScript"
title14.style.color = "purple"
description14.style.background = "yellow"
}

//15
form15.onsubmit = e => {
e.preventDefault()
if (!login15.value || !pass15.value) {
message15.textContent = "Заполните все поля"
} else {
message15.textContent = "Вы успешно вошли"
}
}

//16
let count = 0
btn16.onclick = () => counter16.textContent = ++count

//17
btn17.onclick = () => input17.value = ""

//18
form18.onsubmit = e => {
e.preventDefault()
message18.textContent = "Данные сохранены"
message18.style.color = "green"
}

//19
btn19.onclick = () => {
product19.textContent = "Ноутбук"
price19.textContent = "Цена: 250000 тг"
price19.style.color = "red"
}

//20
form20.onsubmit = e => {
e.preventDefault()
if (!name20.value || !email20.value) {
message20.textContent = "Заполните все поля"
} else {
message20.textContent = "Спасибо за регистрацию, " + name20.value
message20.style.color = "green"
title20.textContent = "Регистрация успешна"
}
}
