#!/usr/bin/node
// It searches second biggest integer in list of arguments.

let biggest = 0;
let v;
const arrayNumbers = [];

for (v = 2; v < process.argv.length; v++) {
  if (Number.isNaN(parseInt(process.argv[v])) === false) {
    arrayNumbers[v - 2] = parseInt(process.argv[v]);
  }
}

if (arrayNumbers.length > 1) {
  biggest = Math.max.apply(null, arrayNumbers);
  v = arrayNumbers.indexOf(biggest);
  arrayNumbers[v] = -Infinity;
  biggest = Math.max.apply(null, arrayNumbers);
}

console.log(biggest);
