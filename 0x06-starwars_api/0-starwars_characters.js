const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}`;

request(url, async (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const charactersArray = JSON.parse(body).characters;
  if (!charactersArray || charactersArray.length === 0) {
    console.log("No characters found for this movie.");
    return;
  }

  for (const character of charactersArray) {
    await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        if (err) {
          console.log(err);
          reject();
        }

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});