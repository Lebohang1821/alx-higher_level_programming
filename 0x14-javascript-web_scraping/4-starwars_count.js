#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API-URL>');
  process.exit(1);
}

// Make a GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const filmsData = JSON.parse(body);

    // Check if the films data is available
    if (filmsData.results) {
      // Filter films where "Wedge Antilles" is present
      const filmsWithWedge = filmsData.results.filter((film) =>
        film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );

      // Print the number of films with "Wedge Antilles"
      console.log(filmsWithWedge.length);
    } else {
      console.log('Unable to fetch films data');
    }
  }
});
