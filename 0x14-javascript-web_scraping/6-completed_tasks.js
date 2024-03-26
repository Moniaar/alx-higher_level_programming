#!/usr/bin/node
const request = require('request');

// Function to compute the number of tasks completed by each user ID
function computeCompletedTasks (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const todos = JSON.parse(body);
      const completedTasks = {
      };

      todos.forEach(todo => {
        if (todo.completed) {
          if (completedTasks[todo.userId]) {
            completedTasks[todo.userId]++;
          } else {
            completedTasks[todo.userId] = 1;
          }
        }
      });

      console.log(completedTasks);
    } else {
      console.error('Error fetching todo data:', error);
    }
  });
}

// Example usage:
const apiUrl = 'https://jsonplaceholder.typicode.com/todos';
computeCompletedTasks(apiUrl);
