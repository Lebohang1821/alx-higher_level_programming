#!/usr/bin/node

const fs = require('fs');

const myfile = process.argv[2];
const content = process.argv[3];

if (!myfile || !content) {
  console.error('Usage: ./1-writeme.js <file-path> <content>');
  process.exit(1);
}

fs.writeFile(myfile, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(`Content written to ${myfile}`);
  }
});
