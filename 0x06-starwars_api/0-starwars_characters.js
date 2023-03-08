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

function returnPromise (link) {
  return new Promise(function (resolve, reject) {
    request(link, function (err, res, body) {
      if (err) {
        console.log(err);
      } else {
        const data = JSON.parse(body);
        resolve(data);
      }
    });
  });
}

async function printCharacters () {
  const films = await returnPromise(url + id);

  for (const link of films.characters) {
    const data = await returnPromise(link);
    console.log(data.name);
  }
}

printCharacters();
