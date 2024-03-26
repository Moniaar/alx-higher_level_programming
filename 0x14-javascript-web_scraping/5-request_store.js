#!/usr/bin/node
const request = require('request');
const fs = require('fs');

// Function to fetch webpage content and store it in a file
function fetchAndSave (url, filePath) {
  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
        if (err) {
          console.error('Error writing to file:', err);
        }
      });
    } else {
      console.error('Error fetching webpage content:', error);
    }
  });
}

// Command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Check if both URL and file path are provided
if (!url || !filePath) {
  console.error('Please provide both a URL and a file path.');
} else {
  fetchAndSave(url, filePath);
}
