#!/usr/bin/node
exports.esrever = function (list) {
  const someArray = [];
  for (const i in list) {
    someArray.push(list[list.length - i - 1]);
  }
  return someArray;
  //  OR
  //  while (list.length) {
  // output.push(list.pop());
  //   }
};
