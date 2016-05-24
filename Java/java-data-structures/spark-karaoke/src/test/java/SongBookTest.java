import org.junit.*;
import static org.junit.Assert.*;

import app.model.SongBook;

public class SongBookTest {

  @Test
  public void SongBook_instantiatesCorrectly() {
    SongBook songBook = new SongBook();
    assertNotNull(songBook);
  }
}