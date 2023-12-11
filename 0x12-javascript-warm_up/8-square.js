#!/usr/bin/node
// It prints square of size x using character 'X'

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let v = 0; v < parseInt(process.argv[2]); v++) {
    console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
