#!/usr/bin/node
// It imports a dictionary of occurrences by user id
const dict = require('./101-data').dict;
const newDict = {};

for (const x in dict) {
  if (newDict[dict[x]] === undefined) { newDict[dict[x]] = []; }
  newDict[dict[x]].push(x);
}
console.log(newDict);
