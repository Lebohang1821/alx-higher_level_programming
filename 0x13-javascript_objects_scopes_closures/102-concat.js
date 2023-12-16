#!/usr/bin/node
// It concats 2 files
// first argument is file path of first source file
// second argument is file path of second source file
// third argument is file path of destination
const fs = require('fs');

const fArg = fs.readFileSync(process.argv[2]).toString();
const sArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], fArg + sArg);
