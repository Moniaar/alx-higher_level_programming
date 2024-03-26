#!/usr/bin/node
const fs = require('fs');

function writeStringToFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    } else {
      console.log('File has been written successfully.');
    }
  });
}

// Extracting file path and content from command line arguments
const args = process.argv.slice(2);
const filePath = args[0];
const content = args[1];

// Checking if both file path and content are provided
if (!filePath || !content) {
  console.error(new Error('Please provide both a file path and content as arguments.'));
} else {
  writeStringToFile(filePath, content);
}
