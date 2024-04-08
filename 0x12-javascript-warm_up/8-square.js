#!/usr/bin/node

// Get the size of the square as the first argument passed to the script (process.argv[2])
const size = parseInt(process.argv[2]);

// Check if size is a valid positive integer
if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  // Loop size times to print each row of the square
  for (let i = 0; i < size; i++) {
    // Use string repetition to print 'X' size times in each row
    console.log('X'.repeat(size));
  }
}
