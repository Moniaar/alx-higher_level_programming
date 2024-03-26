#!/usr/bin/node
// a script that prints all characters of a Star Wars movie
const request = require('request');
const util = require('util');
const filmId = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${
filmId}`;

const prequest = util.promisify(request);

(async () => {
  try {
    const film = (await prequest(URL, { json: true })).body;
    for (const url of film.characters) {
      const character = (await prequest(url, { json: true })).body;
      console.log(character.name);
    }
  } catch (error) {
    console.log(error);
  }
})();
