#!/usr/bin/node

const fs = require('fs');
const myfile = process.argv[2];
const string = process.argv[3];

fs.writeFile(myfile, string, 'utf-8', function (err) {
  if (err) console.log(err);
});
