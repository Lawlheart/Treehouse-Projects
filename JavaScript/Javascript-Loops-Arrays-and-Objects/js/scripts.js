function print(message) {
  var div = document.getElementById("output");
  div.innerHTML = message;
};//prints to output
function studentList() {
	var readout = ""
	var student;
	for(var i=0; i<students.length;i++) {
		readout+="<li>"
		student = students[i]
		for(prop in student) {
			readout += "<p>"+prop.toUpperCase()+": "+student[prop]+"<p>"
		}
		readout+="</li><br />"
	}
	print(readout);
};//prints the list of students to the page
var students = [
	{
		name:'Kenneth',
		track:'Front End Web Development',
		achievements:28,
		points:2502,
	},
	{
		name:'Brigette',
		track:'Front End Web Development',
		achievements:13,
		points:867,
	},
	{
		name:'Amanda',
		track:'Front End Web Development',
		achievements:9,
		points:553,
	},
	{
		name:'Brittany',
		track:'Web Design',
		achievements:145,
		points:10448,
	},
	{
		name:'Amanda',
		track:'Wordpress Development',
		achievements:32,
		points:1974,
	},
];
var response;
var output='';
while(response !== 'quit') {
	response = prompt("Enter a student's name to search records.")
	if(response === null) {break;}
	for(var i=0;i<students.length;i++) {
		var student = students[i]
		console.log(student.name);
		console.log(response);
		if(student.name.toLowerCase()===response.toLowerCase()) {
			output+="<li>"
			for(prop in student) {
				output+=prop.toUpperCase()+": "+student[prop]+"<br />";
			}
			output+="</li><br />"
		}
	}
	print(output);
}
