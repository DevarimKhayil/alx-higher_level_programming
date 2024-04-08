#!/usr/bin/node

// Import the callMeMoby function from the 101-call_me_moby.js file
const callMeMoby = require('./101-call_me_moby').callMeMoby;

// Call the callMeMoby function with arguments 3 (number of times) and a function to print 'C is fun'
callMeMoby(3, function () {
  console.log('C is fun');
});
