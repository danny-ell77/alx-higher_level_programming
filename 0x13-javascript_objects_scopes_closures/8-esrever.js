#!/usr/bin/node
exports.esrever = function (list) {
    some_array = []
    for (let i in list) { 
        some_array.push(list[list.length - i - 1])
    }
    return some_array
    //  OR
    //  while (list.length) {
    // output.push(list.pop());
    //   }

}
