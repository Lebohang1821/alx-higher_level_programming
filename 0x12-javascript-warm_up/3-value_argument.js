#!/usr/bin/node
// It print first argument passed or "No argument" if none

// It gets first argument passed to script
const firstArgument = process.argv[2];

// Console.log(...) to print output
if (firstArgument) {
  console.log(firstArgument);
} else {
  console.log("No argument");
}
