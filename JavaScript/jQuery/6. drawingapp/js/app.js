//problem: user interaction causes no change to application
//solution: when user interacts, cause changes appropriately

var context = $('canvas')[0].getContext("2d")
var $canvas = $('canvas')
var lastxpos;
var lastypos;
var mouseDown = false;
$color = $('.selected').css('background-color')
//takes the value of the sliders and changes it to an rgb color value
function color() {
	return "rgb(" + $('#red').val() + ", " + $('#green').val() + ", " + $('#blue').val() + ")"
}

//function to change color of span to color of slider values
function previewColor() {
	$('#newColor').css('background-color',color());
}

//changes preview color when sliders are changed
$('.sliders input').change(previewColor)

//color list items, when clicked... 
$(".controls").on('click', 'li', function(){
	//deselect sibling elements
	$(this).siblings().removeClass('selected');
	//select clicked element
	$(this).addClass('selected');
	//cache current color
	$color = $(this).css("background-color");
});

//New Color button, when clicked... 
$('#revealColorSelect').click(function(){
	//toggles color select sliders
	$('#colorSelect').toggle();
});

//Add Color button, when clicked...
$('#addNewColor').click(function(){
	//make new li element
	$addedColor = $('<li></li>');
	//changes new li color to new color
	$addedColor.css('background-color', color());
	//Append new color to end of list
	$('.controls ul').append($addedColor);
	//change to new color
	$addedColor.click();
	//hides color select sliders
	$('#colorSelect').hide();
});

//on mouse events on the canvas
	//draw lines
$canvas.mousedown(function(e){
	lastxpos = e.offsetX === undefined ? e.originalEvent.layerX-$('#canvas').offset().left : e.offsetX;
	lastypos = e.offsetY === undefined ? e.originalEvent.layerY-$('#canvas').offset().top : e.offsetY;
	mouseDown=true;
}).mousemove(function(e){
	xpos = e.offsetX === undefined ? e.originalEvent.layerX-$('#canvas').offset().left : e.offsetX;
	ypos = e.offsetY === undefined ? e.originalEvent.layerY-$('#canvas').offset().top : e.offsetY;
	if(mouseDown) {
		context.beginPath();
		context.moveTo(lastxpos,lastypos);
		context.lineTo(xpos, ypos);
		context.strokeStyle = $color
		context.stroke();
		lastxpos = xpos;
		lastypos = ypos;
	}
}).mouseup(function(){
	mouseDown = false;
}).mouseleave(function(){
	mouseDown = false;
})
//add line thickness slider and clear button

