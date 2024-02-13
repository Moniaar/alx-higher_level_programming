#!/usr/bin/node
const process = require('process');
if (process.argv[2] !== undefined) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
