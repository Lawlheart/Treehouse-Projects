var playlist = new Playlist();

var stairwayToHeaven = new Song("Stairway to Heaven", "Led Zeppelin", "8:02");
var bohemianRhapsody = new Song("Bohemian Rhapsody", "Queen", "5:55");
var heyJude = new Song("Hey Jude", "The Beatles", "7:11")
var antMan = new Movie("Ant Man", 2015, "1:57:00")

playlist.add(stairwayToHeaven);
playlist.add(bohemianRhapsody);
playlist.add(heyJude);
playlist.add(antMan);

var playlistElement = document.getElementById("playlist");

playlist.renderInElement(playlistElement);

var playButton = document.getElementById("play");
playButton.onclick = function() {
	playlist.play();
	playlist.renderInElement(playlistElement);

}
var nextButton = document.getElementById("next");
nextButton.onclick = function() {
	playlist.next();
	playlist.renderInElement(playlistElement);
}
var stopButton = document.getElementById("stop");
stopButton.onclick = function() {
	playlist.stop();
	playlist.renderInElement(playlistElement);
}