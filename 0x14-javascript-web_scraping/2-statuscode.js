#!/usr/bin/node
const request = require('request');

function displayGetRequestStatusCode (url) {
  request(url, (error, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log(`code: ${
response.statusCode}`);
    }
  });
}

// Extracting URL from command line arguments
const args = process.argv.slice(2);
const url = args[0];

// Checking if URL is provided
if (!url) {
  console.error(new Error('Please provide a URL as an argument.'));
} else {
  displayGetRequestStatusCode(url);
}
