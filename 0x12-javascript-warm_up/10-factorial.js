#!/usr/bin/node
function factorial (m) {
  if (isNaN(m) || m === 0) return 1;
  return m * factorial(m - 1);
}

console.log(factorial(Number(process.argv[2])));
