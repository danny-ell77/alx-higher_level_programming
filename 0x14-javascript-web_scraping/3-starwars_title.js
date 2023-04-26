#!/usr/bin/node

const request = require('request');
const film_id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${film_id}`, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
