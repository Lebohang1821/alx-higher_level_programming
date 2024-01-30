#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Get the URL from the command line arguments
const URL = process.argv[2];

// Check if a URL is provided
if (!URL) {
  // If not, print a usage message and exit with an error code
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

// Make a GET request to the specified URL
request(URL, function (err, response) {
  // Check if an error occurred during the request
  if (err) {
    // If yes, print the error
    console.log(err);
  } else {
    // If no error, print the status code from the response
    console.log('code: ' + response.statusCode);
  }
});
