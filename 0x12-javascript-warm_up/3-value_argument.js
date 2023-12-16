#!/usr/bin/node

// It print first argument passed or "No argument" if none

if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
