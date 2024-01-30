#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <API-URL>');
  process.exit(1);
}

// Make a GET request to the specified API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // Parse the JSON response
    const todosData = JSON.parse(body);

    // Initialize an object to store the count of completed tasks per user id
    const completedTasksByUser = {};

    // Filter completed tasks and count them per user id
    todosData.forEach((task) => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    // Print the result as a JSON object
    console.log(completedTasksByUser);
  }
});
