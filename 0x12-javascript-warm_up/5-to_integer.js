#!/usr/bin/node

const args = process.argv.slice(2);
const firstArgument = parseInt(args[0]);

if (!isNaN(firstArgument)) {
    console.log(`My number: ${firstArgument}`);
} else {
    console.log("Not a number");
}
