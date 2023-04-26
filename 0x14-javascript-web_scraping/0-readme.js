#!/usr/bin/node

const fs = require('fs');

const filename = process.argv[2];
console.log(filename);

fs.readFile(filename, 'utf8', (err, data) => {
  if (err) return console.log(err);
  console.log(data);
});
