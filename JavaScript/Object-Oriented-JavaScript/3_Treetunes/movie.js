function Movie(title, year, duration) {
	Media.call(this, title, duration)
	this.year = year;
}

Movie.prototype = Object.create(Media.prototype)

Movie.prototype.toHTML = function() {
	var htmlString = '<li '
	if(this.isPlaying === true) {
		htmlString += 'class="current"'
	}
	htmlString += '>'
	htmlString += this.title
	htmlString += ' (' + this.year + ') '
	htmlString += '<span class="duration">' + this.duration + '</span></li>'
	return htmlString;
};