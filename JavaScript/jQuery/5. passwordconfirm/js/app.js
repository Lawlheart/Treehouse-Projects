//problem: popups stay open, might confuse user
//solution: popups need to disappear when requirements are met. Should also add a way to show when errors happen.
var $password = $('#password');
var $confirm = $('#confirm_password')
var $username = $("#username");
//hide hints
$('form span').hide()


function isUsernamePresent() {
  return $username.val().length>0
}
function isPasswordValid() {
	return $password.val().length>8
}

function arePasswordsMatching() {
	return $confirm.val() === $password.val()
}

function canSubmit() {
	return isPasswordValid() && arePasswordsMatching() && isUsernamePresent();
}

function passwordEvent() {
	//find out if password is valid
	if(isPasswordValid()) {
	//hide hint if valid
		$password.next().hide()
	} else {
	//else show hint
		$password.next().show()
	}
}
function confirmEvent(){
	//find oout if confirmation matches password
	if(arePasswordsMatching()) {
		//hide hint if matches
		$confirm.next().hide();
		} else {
		//else show hint 
		$confirm.next().show();
	}
}

function enableSubmitEvent() {
	$('#submit').prop("disabled",!canSubmit())
}

//when event happens on password input
$password.focus(passwordEvent).keyup(passwordEvent).keyup(confirmEvent).keyup(enableSubmitEvent) ;

//when event happens on confirmation
$confirm.focus(confirmEvent).keyup(confirmEvent).keyup(enableSubmitEvent) ;

enableSubmitEvent() 