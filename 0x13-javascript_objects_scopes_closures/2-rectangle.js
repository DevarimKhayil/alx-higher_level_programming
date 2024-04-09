#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (this._isValidDimension(w) && this._isValidDimension(h)) {
      this.width = w;
      this.height = h;
    }
  }

  _isValidDimension (value) {
    return typeof value === 'number' && value > 0;
  }
}

module.exports = Rectangle;
