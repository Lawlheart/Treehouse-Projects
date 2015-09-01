var photoHTML = '';
$(document).ready(function() {


  $('form').submit(function (evt) {
    evt.preventDefault();
    $('#photos').html(" ")
    var flickerAPI = "http://api.flickr.com/services/feeds/photos_public.gne?jsoncallback=?";
    var $searchField = $("#search")
    var $submitButton = $('#submit');
    var searchText = $searchField.val();
    var flickrOptions = {
      tags: searchText,
      format: "json"
    };
    $searchField.prop('disabled', true);
    $submitButton.attr('disabled', true).val('Searching...')
    console.log("searching for: "+searchText);
    function displayPhotos(data) {
      photoHTML = '';
      $.each(data.items,function(i,photo) {
        photoHTML += '<li class="grid-25 tablet-grid-50">';
        photoHTML += '<a href="' + photo.link + '" class="image">';
        photoHTML += '<img src="' + photo.media.m + '"></a></li>';
      }); // end each
      $('#photos').html(photoHTML);
      $searchField.prop('disabled', false);
      $submitButton.attr('disabled', false).val('Search');
      if(photoHTML === "") {
        $('#photos').append($('<p>No results found for '+$searchField.val()+'</p>'))
      };
    }; // end displayPhotos
    $.getJSON(flickerAPI, flickrOptions, displayPhotos);
  }); // end submit

}); // end ready