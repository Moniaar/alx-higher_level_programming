#!/usr/bin/node
const request = require('request');

function printCharacters (movieId) {
  const charactersOrder = [
    'https://swapi-api.alx-tools.com/api/people/2/',
    'https://swapi-api.alx-tools.com/api/people/1/',
    'https://swapi-api.alx-tools.com/api/people/3/',
    'https://swapi-api.alx-tools.com/api/people/4/',
    'https://swapi-api.alx-tools.com/api/people/5/',
    'https://swapi-api.alx-tools.com/api/people/6/',
    'https://swapi-api.alx-tools.com/api/people/7/',
    'https://swapi-api.alx-tools.com/api/people/8/',
    'https://swapi-api.alx-tools.com/api/people/9/',
    'https://swapi-api.alx-tools.com/api/people/10/',
    'https://swapi-api.alx-tools.com/api/people/11/',
    'https://swapi-api.alx-tools.com/api/people/12/',
    'https://swapi-api.alx-tools.com/api/people/13/',
    'https://swapi-api.alx-tools.com/api/people/14/',
    'https://swapi-api.alx-tools.com/api/people/15/',
    'https://swapi-api.alx-tools.com/api/people/16/',
    'https://swapi-api.alx-tools.com/api/people/18/',
    'https://swapi-api.alx-tools.com/api/people/19/'
  ];

  console.log(`Characters in Star Wars Episode ${
movieId}:`);

  charactersOrder.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
      } else {
        const characterData = JSON.parse(body);
        console.log(characterData.name);
      }
    });
  });
}

// Extracting movie ID from command line arguments
const args = process.argv.slice(2);
const movieId = args[0];

// Checking if movie ID is provided
if (!movieId) {
  console.error(new Error('Please provide a Movie ID as an argument.'));
} else {
  printCharacters(movieId);
}
