#!/usr/bin/node
// It prints addition of 2 integers
// The first argument is first integer
// The second argument is second integer

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]));
