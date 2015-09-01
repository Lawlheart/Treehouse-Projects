function Quiz () {
	this.questions = []
	this.progress = 0;
	this.score = 0;
}

Quiz.prototype.guess = function(guess) {
	var question = this.questions[this.progress];
	var answer = question.answer;
	if(guess === answer) {
		this.score += 1;
	}
	this.progress += 1;
	if(this.progress < this.questions.length ) {
		quiz.renderInElement();
	} else {
		quiz.renderScorePage();
	}
}

Quiz.prototype.add = function(question) {
	this.questions.push(question);
};

Quiz.prototype.renderInElement = function() {
	var question = this.questions[this.progress]
	var HTML ='<h1>Persona Quiz</h1>';
	HTML += question.toHTML();
	HTML += '<footer><p id="progress">Question '+(this.progress+1)+' of '+ this.questions.length + '</p></footer>';
	this.populateIdWithHTML("quiz", HTML)
};
Quiz.prototype.renderScorePage = function() {
	var HTML ='<h1>Persona Quiz</h1>';
	HTML += '<h2 id="score" class="headline-secondary--grouped">Score: ' + this.score + ' out of ' + this.questions.length + '</h2>';
	this.populateIdWithHTML("quiz", HTML);
}
Quiz.prototype.populateIdWithHTML = function(id, text) {
	var element = document.getElementById(id);
	element.innerHTML = text;
}

//Bad code :'(  
	// Quiz.prototype.bindButtons = function() {
	// 	var buttons = document.getElementsByTagName("button");
	// 	for(var i=0;i<buttons.length;i++){
	// 		var button = buttons[i]
	// 		buttons[i].onclick = function() {
	// 			button.className += ' selected'
	// 			var guess = document.getElementsByClassName('selected')[0].innerHTML
	// 			console.log(guess)
	// 			quiz.guess(guess)
	// 		}
	// 	}
	// 