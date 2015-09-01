var quiz = new Quiz();

var question1 = new Question("What is the name of the homeroom teacher at the start of Persona 4 Golden?", "Kinshiro Morooka", ["Noriko Kashiwagi", "Kimiko Sofue" , "Kinshiro Morooka"])
var question2 = new Question("What is the name of the first Persona that the Protagonist summons?", "Izanagi", ["Jiraiya","Izanami","Izanagi", "Teddie"])

quiz.add(question1)
quiz.add(question2)


quiz.renderInElement();