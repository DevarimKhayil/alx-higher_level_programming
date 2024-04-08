#!/usr/bin/node

// Import the addMeMaybe function from the 102-add_me_maybe.js file
const addMeMaybe = require('./102-add_me_maybe').addMeMaybe;

// Call the addMeMaybe function with argument 4 and a function to print the new value
addMeMaybe(4, function (nb) {
  console.log('New value: ' + nb);
});
