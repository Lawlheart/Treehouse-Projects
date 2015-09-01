$(".animsition").animsition({
	inClass: "fade-in-up-sm",
	outClass: "fade-out-down-sm",
	linkElement: "header a",
	inDuration: 500,
	outDuration: 400
});

$(".header").sticky({
	getWidth: '.container',
	responsiveWidth: true
}).on('sticky-start', function() {
	$(".description").html("We build <strong>super</strong> apps!")
}).on('sticky-end', function() {
	$(".description").html("We build apps")
});

$(".work").sticky({
	topSpacing:64,
	getWidth: '.container',
	responsiveWidth: true
}).on('sticky-start', function() {
	$(this).append(" <a href='mailto:email@website.com' class='email-text'>Email&nbsp;us</a>")
}).on('sticky-end', function() {
	$(".email-text").remove();
});

