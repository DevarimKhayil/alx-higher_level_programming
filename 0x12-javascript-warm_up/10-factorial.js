#!/usr/bin/node

// Define the factorial function using recursion
function factorial (n) {
  if (isNaN(n)) {
    return 1; // Factorial of NaN is 1
  }
  if (n <= 1) {
    return 1; // Factorial of 0 or 1 is 1
  }
  return n * factorial(n - 1); // Recursive call to compute factorial
}

// Get the integer as an argument passed to the script (process.argv[2])
const num = parseInt(process.argv[2]);

// Print the factorial of num using the factorial function
console.log(factorial(num));
