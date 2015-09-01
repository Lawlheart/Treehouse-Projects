var main = function() {
	var number = 1
	$(':button#add').click(function(){
		$('<li>').text('List #'+number).appendTo('#output');
		number++;
	});
	$('#output').on('click','li',function(){
		$('li').removeClass('selected');
		$(this).addClass('selected');
	});
	$(':button#remove').click(function(){
		$('.selected').remove();
	});
};

$(document).ready(main);