#!/usr/bin/node

// Get the first argument passed to the script (process.argv[2])
const myArg = process.argv[2];

// Check if myArg is undefined (no argument passed) and print the appropriate message
if (myArg === undefined) {
    console.log("No argument");
} else {
    console.log(myArg);
}
