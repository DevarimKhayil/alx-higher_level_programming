#!/usr/bin/node

// Define the addMeMaybe function that takes two parameters: number and theFunction
function addMeMaybe (number, theFunction) {
  // Increment the number parameter by 1
  const newNumber = number + 1;

  // Call theFunction with the newNumber as an argument
  theFunction(newNumber);
}

// Make the addMeMaybe function visible outside by exporting it
module.exports = {
  addMeMaybe
};
