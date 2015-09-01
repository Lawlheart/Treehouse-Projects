$(document).ready(function() {
	$.getJSON('data/employees.json', function(response) {
		var statusHTML = '<ul class="bulleted">'
		$.each(response, function(index, employee) {
			if(employee.inoffice) {
				statusHTML += '<li class="in">'
			} else {
				statusHTML += '<li class="out">';
			};
			statusHTML += employee.name+'</li>';
		});//end each
		statusHTML += '</ul>'
		$('#employeeList').html(statusHTML);
	});//end getJSON
});//end ready