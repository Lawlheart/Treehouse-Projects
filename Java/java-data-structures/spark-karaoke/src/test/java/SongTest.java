import org.junit.*;
import static org.junit.Assert.*;

import app.model.Song;

public class SongTest {

  @Test 
  public void Song_instantiatesCorrectly() {
    Song song = new Song("Artist", "Title", "http://video.url");
    assertEquals("Artist", song.getArtist());
    assertEquals("Title", song.getTitle());
    assertEquals("http://video.url", song.getVideoUrl());
  }

}