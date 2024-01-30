#!/usr/bin/env node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./3-starwars_title.js <movie-ID>');
  process.exit(1);
}

// Construct the URL for the Star Wars API with the specified movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const movieData = JSON.parse(body);

    // Check if the movie data is available
    if (movieData.title) {
      // If yes, print the title
      console.log(movieData.title);
    } else {
      console.log('Movie not found');
    }
  }
});
