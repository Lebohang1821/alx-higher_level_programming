#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

// Import the 'request' module for making HTTP requests
const request = require('request');

// Get the movie ID from the command line arguments
const film = process.argv[2];

// Construct the URL for the Star Wars movie using the specified movie ID
const url = `https://swapi-api.hbtn.io/api/films/${film}`;

// Make a GET request to the Star Wars API to fetch information about the specified movie
request(url, (err, res, body) => {
  // Check if there is no error in the request
  if (!err) {
    // Parse the JSON response to get the characters of the movie
    const characters = JSON.parse(body).characters;

    // Iterate over each character URL
    characters.forEach((character) => {
      // Make a GET request to the character URL
      request(character, function (err, res, body) {
        // Check if there is no error in the request
        if (!err) {
          // Parse the JSON response and print the character's name
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
