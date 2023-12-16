#!/usr/bin/node
// It executes x times a function

exports.callMeMoby = function (x, theFunction) {
  for (let v = 0; v < x; v++) theFunction();
};
