#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const i in list) {
    if (searchElement === list[i]) {
      count++;
    }
  }
  return count;
  // OR
  // list.reduce((count, item) => item === searchElement ? count + 1 : count, 0)
};
