#!/usr/bin/node

// Define the add function with parameters a and b
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

// Get the first and second integers as arguments passed to the script (process.argv[2] and process.argv[3])
const num1 = process.argv[2];
const num2 = process.argv[3];

// Print the result of adding num1 and num2 using the add function
console.log(add(num1, num2));
