//1
let numbers = [3, 7, 12, 5, -2, 20, 8];


let numbers1 = numbers.map(num => num * 3);
console.log(numbers1);

// 2
let ten = numbers.filter(num => num > 10);
console.log(ten);

// 3
let firstfive= numbers.find(num => num % 5 === 0);
console.log(firstfive);

// 4
let minus = numbers.some(num => num < 0);
console.log(minus);

// 5
let evennum = numbers.every(num => num % 2 === 0);
console.log(evennum);

// 6
let sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum);



// 2/

let words = ["apple", "banana", "kiwi", "strawberry", "melon"];

// 1
let upperfruits= words.map(word => word.toUpperCase());
console.log(upperfruits);

// 2
let longWords = words.filter(word => word.length > 5);
console.log("Длиннее 5:", longWords);

// 3
let firstlong = words.find(word => word.length > 7);
console.log(firstlong);


//3/
let users = [
  { name: "Ali", age: 17, isActive: true },
  { name: "Dana", age: 22, isActive: false },
  { name: "Aruzhan", age: 19, isActive: true },
  { name: "Maksat", age: 15, isActive: true }
];

// 1
let names = users.map(user => user.name);
console.log(names);

// 2
let activeUsers = users.filter(user => user.isActive);
console.log("Активные:", activeUsers);

// 3
let adults = users.filter(user => user.age > 18);
console.log(adults);

// 4
let firstoffline = users.find(user => !user.isActive);
console.log(firstoffline);

// 5
let sixteen = users.some(user => user.age < 16);
console.log(sixteen);

// 6
let allActive = users.every(user => user.isActive);
console.log(allActive);

// 7
let totalAge = users.reduce((acc, user) => acc + user.age, 0);
console.log(totalAge);
