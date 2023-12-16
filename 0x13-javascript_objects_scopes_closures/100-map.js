#!/usr/bin/node
// It imports an array and computes a new array.
const list = require('./100-data').list;
const newList = list.map(function (numb, index) {
  return numb * index;
});

console.log(list);
console.log(newList);
