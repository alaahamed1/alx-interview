#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + String(movieID);

request(url, (err, resp, body) => {
  if (!err) {
    const urlChars = JSON.parse(body).characters;
    printInOrder(urlChars, 0);
  }
});

const printInOrder = (urlChars, index) => {
  if (index === urlChars.length) return;
  request(urlChars[index], (err, resp, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      printInOrder(urlChars, index + 1);
    }
  });
};
