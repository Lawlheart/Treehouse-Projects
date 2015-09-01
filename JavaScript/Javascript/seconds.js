var secondsPerMin = 60;
var minsPerHour = 60;
var hoursPerDay = 24;
var daysPerWeek = 7;
var weeksPerYear = 52;
var secondsPerDay = secondsPerMin*minsPerHour*hoursPerDay;
document.write("<p>There are " + secondsPerDay + " seconds in a day.</p>");
var yearsAlive = 26;
var secondsAlive = yearsAlive * weeksPerYear * daysPerWeek * hoursPerDay * minsPerHour * secondsPerMin;

document.write('<p>I\'ve been alive more than ' + Math.floor(secondsAlive) + ' seconds.</p>');

var billionthSecond = 1000000000  / secondsPerDay / daysPerWeek / weeksPerYear;

var yearinBilUn = billionthSecond;
var yearinBil = Math.floor(yearinBilUn);

var daysinBilUn = (billionthSecond - yearinBil) * (weeksPerYear * daysPerWeek);
var daysinBil = Math.floor(daysinBilUn);

var hoursinBilUn = (daysinBilUn - daysinBil) *hoursPerDay;
var hoursinBil = Math.floor(hoursinBilUn);

var minsinBilUn = (hoursinBilUn-hoursinBil)*minsPerHour;
var minsinBil = Math.floor(minsinBilUn);

var secondsinBilUn = (minsinBilUn-minsinBil)*secondsPerMin;
var secondsinBil = Math.floor(secondsinBilUn);

monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
endDays = [31,28,31,30,31,30,31,31,30,31,30,31];
var date = 0;

var month = function(days) {
	var totalDays=0;
	if(days>0 && days<=365) {
		for(var i=0;i<12;i++) {
			totalDays += endDays[i];	
			if (days<totalDays) {
				return monthNames[i] + " " + (endDays[i]-totalDays%days);
			}
		}	
	}
}
var getDays = function(m,d) {
	if(0<m && m<=12 && 0<d && d<=endDays[(m-1)]) {
		if(m===1) {
			return d
		} else {
			var total=0;
			for(var i=0; i<(m-1);i++) {
				total+=endDays[i];
			}
			return total+d
		}
	} else {
		return "INVALID DATE";
	}
}
console.log(month(283 - getDays(6,29)));

document.write('<p>My 1 billionth second happens when I am ' + yearinBil + ' years and ' + (daysinBil-7) + ' days, '+hoursinBil+' hours, '+minsinBil+' minutes, and '+secondsinBil+' seconds old</p>'); 
document.write('<p> That will be on ' + month(283 - getDays(6,29)) + ', ' + (1988+32) + ' at 11pm </p>')
 

