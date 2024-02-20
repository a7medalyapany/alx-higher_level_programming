#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  // Function to make requests to get character names
  const getCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (charError, charResponse, charBody) => {
        if (charError) {
          reject(charError);
          return;
        }

        if (charResponse.statusCode !== 200) {
          reject(`Error: ${charResponse.statusCode}`);
          return;
        }

        const character = JSON.parse(charBody);
        resolve(character.name);
      });
    });
  };

  // Map each character URL to a promise to fetch the character name
  const promises = charactersUrls.map((characterUrl) => getCharacterName(characterUrl));

  // Wait for all promises to resolve
  Promise.all(promises)
    .then((characters) => {
      characters.forEach((character) => console.log(character));
    })
    .catch((error) => {
      console.error(error);
    });
});
