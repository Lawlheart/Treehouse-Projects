$(document).ready(function () {
	// user clicks a button
	$('button').click(function () {
		// retrieve word on button
		var searchText = $(this).text();
		console.log("Searching for: "+searchText)
		// remove selected class on other buttons
		$('button').removeClass('selected');
		// change color of buton
		$(this).addClass('selected');
		// make a get request to flickr with the word
		$.getJSON('https://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?', {
			tags: searchText,
			format: 'json'
		}, function (data) {
			// recieve JSON response
			var resultsList = data.items;
			console.log(results);
			// add a link and an img tag to the page
			//make the unordered list
			var output = $('<ul></ul>')
			for(var i=0;i<resultsList.length;i++) {
				var results = resultsList[i];
				//make each list item
				var listItem = $('<li class="grid-25 tablet-grid-50"></li>')
				//make each anchor
				var link = $('<a class="image"></a>').prop('href', results.link);
				//make each image
				var img = $('<img></img>').prop('src', results.media.m);
				//append the image to the anchor, then the anchor to the list item, then the list item to the unordered list
				output.append(listItem.append(link.append(img)));
			}; // end for loop
			//clear the previous search results
			$('#photos').html(" ")
			//append the unordered list to the photos div
			$('#photos').append(output)
		}); // end getJSON
	}); // end click
}); //end ready