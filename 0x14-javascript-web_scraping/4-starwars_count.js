#!/usr/bin/node
const request = require('request');

// Function to get the number of movies where the character "Wedge Antilles" is present
function getMoviesWithWedge (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const films = JSON.parse(body).results;
      const wedgeFilms = films.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
      console.log(wedgeFilms.length);
    } else {
      console.log('Error fetching movie details:', error);
    }
  });
}
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
getMoviesWithWedge(apiUrl);
