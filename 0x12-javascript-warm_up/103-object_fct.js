#!/usr/bin/node

// Define the myObject object with type and value properties
const myObject = {
  type: 'object',
  value: 12,
  // Define the incr function within myObject that increments the value property
  incr: function () {
    this.value++; // Increment the value property by 1
  }
};

console.log(myObject);

// Call the incr function to increment the value property
myObject.incr();
console.log(myObject);

// Call the incr function again to increment the value property further
myObject.incr();
console.log(myObject);

// Call the incr function once more to increment the value property again
myObject.incr();
console.log(myObject);
