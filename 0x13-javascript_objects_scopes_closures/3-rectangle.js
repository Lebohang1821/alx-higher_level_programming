#!/usr/bin/node
//defines a rectangle:
//Create an instance method called print() that prints the rectangle using the character X
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let s = '';
      for (let l = 0; l < this.width; l++) {
        s += 'X';
      }
      console.log(s);
    }
  }
}

module.exports = Rectangle;
