#!/usr/bin/node
// reads and prints the content of a file

const fs = require("node:fs");

const fileContent = fs.readFile(process.argv[2], "utf-8", (error, data) => {
	if (error) {
		console.log(error);
	} else {
		console.log(data);
	}
});
