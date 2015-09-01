//problem: it looks gross in smaller browser widths/devices
//solution: hide the text links and swap them out with a more appropriate navigation.

//create a select element and append to menu
var $select = $('<select></select>');
$('#menu').append($select);

//add the list items to the options in the select menu
$('#menu li').each(function(){
	var $anchor = $(this).children()
	//create an option
	var $option = $('<option></option>')

	/*deal with selected options depending on current page*/

if($anchor.parent().hasClass("selected")) {
	$option.prop('selected', true)
}
	//option value is the href of the link
	$option.val($anchor.attr('href'))
	//option text is the text of the link)
	$option.text($anchor.text());
	//append option to select
	$select.append($option)

});

//go to the select's location on change select
var $button= $('<button>Go</button>')

$select.change(function(){
	window.location = $select.val();

});