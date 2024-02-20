#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const films = JSON.parse(body).results;
  const numMovies = films.reduce((count, film) => {
    if (
      film.characters.includes(`https://swapi-api.alx-tools.com/
	                            api/people/${characterId}/`)
    ) {
      return count + 1;
    }
    return count;
  }, 0);

  console.log(numMovies);
});
