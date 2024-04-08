#!/usr/bin/node

// Get the first and second arguments passed to the script (process.argv[2] and process.argv[3])
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Check if both arguments are defined and print them in the specified format
if (arg1 !== undefined && arg2 !== undefined) {
  console.log(`${arg1} is ${arg2}`);
} else {
  console.log(`${arg1} is undefined`);
}
