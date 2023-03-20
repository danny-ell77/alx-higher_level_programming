#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let someString = '';
    for (let h = 0; h < this.height; h++) {
      for (let w = 0; w < this.width; w++) {
        someString += 'X';
      }
      console.log(someString);
      someString = '';
    }
  }
};
