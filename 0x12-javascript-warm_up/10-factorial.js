#!/usr/bin/node

// It computes and prints factorial.
// First argument is integer (argument can be cast as integer)
// Factorial of NaN is 1

function factorial (n) {
  if ((isNaN(n)) || (n === 1)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
