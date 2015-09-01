//problem: when clicking image, goes to a dead end
//solution: create a lightbox

//Create Overlay
var $overlay = $('<div id="overlay"></div>');
//Add image to overlay
var $image = $('<img>');
$overlay.append($image);
//add video to overlay
var $video = $('<video>')
$overlay.append($video)
//add caption to overlay
var $caption = $('<p>')
$overlay.append($caption)
//Add overlay to body
$('body').append($overlay)


// Capture the click event on a link to an image
$('#imageGallery a').click(function(event) {
  event.preventDefault()
  var imageLocation = $(this).attr("href");
  //update overlay with the image linked in the link
  $image.attr('src',imageLocation)
  //get child's alt attribute and set caption
  var caption = $(this).children('img').attr('alt')
  $caption.text(caption)
  //show the overlay
  $video.hide();
  $image.show();
  $overlay.show();
})

// Capture the click event on a link to a video
$('#videos a').click(function(event) {
  event.preventDefault()
  var videoLocation = $(this).attr("href");
  //update overlay with the video linked in the link
  $video.attr('src',videoLocation)
  //get child's alt attribute and set caption
  var caption = $(this).children('img').attr('alt')
  $caption.text(caption)
  $image.hide();
  $video.show();
  //show the overlay
  $overlay.show();
  //play the video
  $video[0].play();
})




//When overlay is clicked
$overlay.click(function(){
  //Hide the overlay
  $overlay.hide();
  $video[0].pause();
});