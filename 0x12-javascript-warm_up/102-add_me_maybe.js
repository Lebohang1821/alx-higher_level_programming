#!/usr/bin/node
// It increments and calls a function

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
