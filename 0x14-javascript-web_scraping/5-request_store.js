#!/usr/bin/env node

const fs = require('fs');
const request = require('request');

// Get the URL and file path from the command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file-path>');
  process.exit(1);
}

// Make a GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Write the response body to the specified file path in UTF-8 encoding
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(writeError);
      } else {
        console.log(`Contents of the webpage saved to ${filePath}`);
      }
    });
  }
});
