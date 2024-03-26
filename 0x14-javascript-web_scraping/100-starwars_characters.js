#!/usr/bin/node
const request = require('request');

function printCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${
movieId}/`;
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    } else {
      const movie = JSON.parse(body);
      movie.characters.forEach(character => {
        request(character, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(charError);
          } else {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          }
        });
      });
    }
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
