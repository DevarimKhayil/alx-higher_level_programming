#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    // If c is undefined, use 'X' as the character
    const char = c || 'X';

    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
