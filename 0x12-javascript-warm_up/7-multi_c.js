#!/usr/bin/node

const max = Number(process.argv[2]);
let i = 0;

if (max) {
  while (i < max) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurences');
}
