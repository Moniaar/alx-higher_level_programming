#!/usr/bin/node
let logCount = 0;
exports.logMe = function (item) { console.log(`${logCount++}: ${item}`); };
