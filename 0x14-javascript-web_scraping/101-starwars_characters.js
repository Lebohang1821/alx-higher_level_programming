#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

// Construct the URL for the Star Wars movie using the specified movie ID from the command line arguments
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

// Function to print characters recursively
function printCharacters(characters, idx) {
  // Make a GET request to the character URL
  request(characters[idx], (err, res, body) => {
    // Check if there is an error in the request
    if (err) {
      console.log(err);
    } else {
      // Parse the JSON response and print the character's name
      console.log(JSON.parse(body).name);

      // If there are more characters, call the function recursively for the next character
      if (idx + 1 < characters.length) {
        printCharacters(characters, idx + 1);
      }
    }
  });
}

// Make a GET request to the Star Wars API to fetch information about the specified movie
request(url, (err, res, body) => {
  // Check if there is an error in the request
  if (err) {
    console.log(err);
  } else {
    // Parse the JSON response to get the characters of the movie
    const characters = JSON.parse(body).characters;

    // Start printing characters with the first character at index 0
    printCharacters(characters, 0);
  }
});
