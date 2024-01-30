#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];

if (!URL) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

request(URL, (error, response) => {
  console.error(error ? error : `code: ${response.statusCode}`);
});
