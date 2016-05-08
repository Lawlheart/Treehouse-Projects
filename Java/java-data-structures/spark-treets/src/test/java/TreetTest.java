import java.util.Arrays;
import java.util.Date;

import org.junit.*;
import static org.junit.Assert.*;

import app.Treet;

public class TreetTest {

  @Test
  public void Treet_instantiatesCorrectly() {
    Treet treet = new Treet("John Doe",
      "This is my Tweet", 
      new Date(1421849732000L));
    assertEquals("John Doe", treet.getAuthor());
    assertEquals("This is my Tweet", treet.getDescription());
    assertEquals(new Date(1421849732000L), treet.getCreationDate());
  }

  @Test
  public void Treet_sortsCorrectly() {
    Treet treet1 = new Treet("John Doe",
      "This is my Tweet", 
      new Date(1421849732000L));
    Treet treet2 = new Treet("Jane Doe",
      "This is my totally other Tweet", 
      new Date(1421878767000L));
    Treet treet3 = new Treet("Tim",
      "All your Tweets are belong to us!", 
      new Date(1421878767000L));
    Treet[] treets = {treet2, treet1};
    Treet[] treetsThreeSides = {treet1, treet2, treet3};
    Arrays.sort(treets);
    Arrays.sort(treetsThreeSides);
    assertEquals(treet1, treets[0]);
    assertEquals(treet3, treetsThreeSides[1]);

  }
}
