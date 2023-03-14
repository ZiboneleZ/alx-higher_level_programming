#!/usr/bin/node

const max = Number(process.argv[2]);
let i = 0;

if (max) {
  while (i < process.argv[2]) {
    console.log(Array(max + 1).join('X'));
    i++;
  }
} else {
  console.log('Missing size');
}
