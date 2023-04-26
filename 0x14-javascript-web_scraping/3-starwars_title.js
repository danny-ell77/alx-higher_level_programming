#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${filmId}`, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
