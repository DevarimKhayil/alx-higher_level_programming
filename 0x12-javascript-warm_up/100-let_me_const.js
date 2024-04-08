#!/usr/bin/node

// Assign the value 89 to the global variable myVar
myVar = 89;

// Require the 100-let_me_const.js file, which modifies myVar to 333
require('./100-let_me_const');

// Print the value of myVar after modification
console.log(myVar);
