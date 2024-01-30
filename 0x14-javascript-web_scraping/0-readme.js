#!/usr/bin/node

const fs = require('fs');

const myfile = process.argv[2];

if (!myfile) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}

fs.readFile(myfile, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
