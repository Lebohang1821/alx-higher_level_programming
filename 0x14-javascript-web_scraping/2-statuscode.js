#!/usr/bin/node

const my_request = require('my_request');

const URL = process.argv[2];

my_request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
