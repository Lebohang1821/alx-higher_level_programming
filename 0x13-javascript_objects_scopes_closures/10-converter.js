#!/usr/bin/node
// It converts number from base 10 to another base passed as argument
exports.converter = function (base) {
  return function (numb) {
    return numb.toString(base);
  };
};
