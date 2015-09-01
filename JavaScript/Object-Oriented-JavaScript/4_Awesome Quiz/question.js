function Question(question, answer, choices) {
	this.question = question;
	this.answer = answer;
	this.choices = choices;
}

Question.prototype.toHTML = function() {
	var HTML = '<h2 id="question" class="headline-secondary--grouped">';
	HTML += this.question;
	HTML += '</h2>';
	for(var i=0;i<this.choices.length;i++) {
		var choice = this.choices[i]
		HTML += '<button id="guess'+ i +'" '
		HTML += 'class="btn--default"' 
		HTML += 'onclick="quiz.guess(\'' + choice + '\')">'
		HTML += choice;
		HTML += '</button>'
	}
	return HTML
}
