#!/usr/bin/node
/*
 * 1. The first argument is the Movie ID - example: 3 = “Return of the Jedi”
 * 2. Display one character name by line
 * 3. You must use the Star wars API
 * 4. You must use the module request
 */

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + id, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const character = data.characters;
  for (const i of character) {
    request(i, function (err, res, body1) {
      if (err) {
        console.log(err);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
