#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    let someString = '';
    if (!c) {
      c = 'X';
    }
    for (let h = this.height; h > 0; h--) {
      for (let w = this.width; w > 0; w--) {
        someString += c;
      }
      console.log(someString);
      someString = '';
    }
  }
};
