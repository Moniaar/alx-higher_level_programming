#!/usr/bin/node
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.log('Please provide a movie ID as an argument.');
  process.exit(1);
}

function getMovieTitle (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${
movieId}/`;

  request(url, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const movie = JSON.parse(body);
      console.log(movie.title);
    } else {
      console.log('Error fetching movie details:', error);
    }
  });
}

getMovieTitle(movieId);
