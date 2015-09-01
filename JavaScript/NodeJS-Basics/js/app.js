var profile = require("./profile.js");
var users = process.argv.slice(2);
// var users = ["kennethblack", "brigetteeckert", "samueldurfey"]
users.forEach(profile.get);


