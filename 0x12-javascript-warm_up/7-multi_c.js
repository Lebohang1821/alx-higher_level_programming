#!/usr/bin/node

// It print "C is fun" x times, where x is first argument

const lang = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let v = 0; v < parseInt(process.argv[2]); v++) {
    console.log(lang);
  }
}
