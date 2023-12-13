#!/usr/bin/node
// It defines a square and inherits from Square of 5-square.js
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      let s = '';
      for (let l = 0; l < this.width; l++) {
        s += c;
      }
      console.log(s);
    }
  }
}

module.exports = Square;
