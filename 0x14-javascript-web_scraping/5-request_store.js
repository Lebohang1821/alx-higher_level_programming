#!/usr/bin/node

// Import the 'fs' (file system) module for file-related operations
const fs = require('fs');

// Import the 'request' module for making HTTP requests
const request = require('request');

// Make a GET request to the URL provided as the first command line argument,
// and pipe the response directly to a writable stream created using the
// 'fs.createWriteStream' function with the file path provided as the second
// command line argument.
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
