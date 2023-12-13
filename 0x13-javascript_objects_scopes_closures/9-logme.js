#!/usr/bin/node
// It prints the number of arguments already printed
let argCount = 0;

exports.logMe = function (item) {
  console.log(`${argCount}: ${item}`);
  argCount++;
};
