#!/usr/bin/node
const fs = require('fs');

function readFileContent (filePath) {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}

// Extracting the file path from the command line arguments
const args = process.argv.slice(2); // Removing the first two arguments (node and script file)
const filePath = args[0];

if (!filePath) {
  console.error(new Error('Please provide a file path as an argument.'));
} else {
  readFileContent(filePath);
}
