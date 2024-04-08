#!/usr/bin/node

// Get the list of arguments passed to the script (process.argv)
const args = process.argv.slice(2); // Exclude the first two arguments (Node.js executable and script name)

// Check if there are no arguments or only one argument
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  // Sort the arguments in ascending order
  args.sort((a, b) => a - b);

  // Print the second last argument (second biggest integer)
  console.log(args[args.length - 2]);
}
