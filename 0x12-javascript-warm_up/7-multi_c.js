#!/usr/bin/node

// Get the first argument passed to the script (process.argv[2])
const numOccurrences = parseInt(process.argv[2]);

// Check if numOccurrences is a valid positive integer
if (isNaN(numOccurrences) || numOccurrences <= 0) {
  console.log('Missing number of occurrences');
} else {
  // Loop numOccurrences times and print "C is fun" each time
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
}
