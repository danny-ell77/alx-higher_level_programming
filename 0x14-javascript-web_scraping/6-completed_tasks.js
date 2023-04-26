#!/usr/bin/node
const fs = require('fs');
const request = require('request');


const filename = process.argv[3];

let content;

request(process.argv[2], function (error, response, body) {
	if (error) throw error;
	body.reduce((a, c) => {
			if (c.completed == true){
				a[c.userId] 
			}
		}, 
		{}
	)
});
