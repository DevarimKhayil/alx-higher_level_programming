#!/usr/bin/node

// Get the first argument passed to the script (process.argv[2])
const arg = process.argv[2];

// Check if the argument can be converted to an integer using parseInt()
if (!isNaN(parseInt(arg))) {
  console.log(`My number: ${parseInt(arg)}`);
} else {
  console.log('Not a number');
}
