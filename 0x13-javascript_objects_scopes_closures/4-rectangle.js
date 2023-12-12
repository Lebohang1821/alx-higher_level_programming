#!/usr/bin/node
// It defines a rectangle:
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
  
  rotate () {
      const aux = this.width;
      this.width = this.height;
      this.height = aux;
  }
  
  double () {
      this.width *= 2;
      this.height *= 2;
  }
}

module.exports = Rectangle;
