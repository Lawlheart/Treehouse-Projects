//Problem: We need a simple way to look at a user's badge count and JavaScript points
//Solution: Use node.js to connect to Treehouse's API to get profile information to print out
var http = require("http");

//print out message
function printMessage(username, badgeCount, points) {
	var message = username + " has " + badgeCount + " total badges and " + points + " total points.";
	console.log(message);
}
//print out errors
function printError (err) {
	console.error(err.message);
}

//Connect to API URL(http://teamtreehouse.com/username.json)

function get(username) {
	var req = http.get("http://teamtreehouse.com/" + username + ".json", function (res) {
		//Read the data
		var body = "";
		res.on('data', function (chunk) {
	    body += chunk;
	 	}).on('end', function () {
	 		if(res.statusCode === 200) {
		 		try {
		 			//Parse the data
			 		var profile = JSON.parse(body);
			 		//Print the data
			 		printMessage(username, profile.badges.length, profile.points.total);
		 		} catch(err) {
		 			//parse Error
		 			printError(err);
		 		}
		 	} else {
		 		//status code error
		 		printError({message: "There was an error getting the profile for " + username + ". [" + http.STATUS_CODES[res.statusCode] + "]"})
		 	}
	 	});
	}).on("error", function (err) {
		printError(err);
	});
}

module.exports.get = get;