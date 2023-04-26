#!/usr/bin/node

const request = require('request');
const baseUrl = process.argv[2];
const characterUri = 'https://swapi-api.alx-tools.com/api/people/18/';

request(baseUrl, function (error, response, body) {
  if (error) throw error;
  const payload = JSON.parse(body);
  const film_count = payload.results.reduce((a, c) => {
    if (c.characters.includes(characterUri)) {
      return a + 1;
    }
    return a;
  }, 0);
  console.log(film_count);
});
