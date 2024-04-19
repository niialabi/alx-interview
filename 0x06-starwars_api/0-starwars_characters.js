#!/usr/bin/node

const request = require('request');

const filmID = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${filmID}/`;

request(url, async (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  console.log(response.statusCode)
  const data = (JSON.parse(body)).characters;
  for (const link of data) {
    const charNamePromise = new Promise((resolve, reject) => {
      request(link, function (error, response, body) {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
    console.log(await charNamePromise)
  };
});
