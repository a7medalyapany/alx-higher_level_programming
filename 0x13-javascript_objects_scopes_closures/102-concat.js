#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: node 102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) throw err;

  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) throw err;

    const concatenatedContent = dataA + '\n' + dataB;

    fs.writeFile(fileC, concatenatedContent, 'utf8', (err) => {
      if (err) throw err;
      console.log('The files have been concatenated and saved to', fileC);
    });
  });
});
