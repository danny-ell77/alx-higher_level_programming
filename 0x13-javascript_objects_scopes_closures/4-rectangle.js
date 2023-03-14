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
    for (let h = this.height; h > 0; h--) {
      for (let w = this.width; w > 0; w--) {
        someString += 'X';
      }
      console.log(someString);
      someString = '';
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
