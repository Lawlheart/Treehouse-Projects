function Dice(sides) {
	this.sides = sides;
}

Dice.prototype.roll = function() {
	var randomNumber = Math.floor(Math.random() * this.sides) + 1;
	return randomNumber
}

var d6 = new Dice(6);

function stats() {
	var stats = [];
	for(var i=0;i<6;i++) {
		var stat = [d6.roll(), d6.roll(), d6.roll(), d6.roll()];
		var stat = stat.sort();
		var stat = stat[1]+stat[2]+stat[3]
		stats.push(stat)
	}
	return stats
}
console.log(stats())