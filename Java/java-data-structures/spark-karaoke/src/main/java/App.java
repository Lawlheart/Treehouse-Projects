import java.util.HashMap;
import java.util.Map;

import spark.ModelAndView;
import spark.template.velocity.VelocityTemplateEngine;
import static spark.Spark.*;

import app.model.Song;
import app.model.SongBook;

public class App {
  public static void main(String[] args) {
    staticFileLocation("/public");
    String layout = "templates/layout.vtl";

    Song song = new Song(
      "Michael Jackson", 
      "Beat It", 
      "https://www.youtube.com/watch?v=SaEC9i9QOvk");
    SongBook songBook = new SongBook();
    songBook.addSong(song);

    get("/", (request, response) -> {
      Map<String, Object> model = new HashMap<>();
      model.put("template", "templates/index.vtl");
      model.put("song", song);
      model.put("songbook", songBook);
      return new ModelAndView(model, layout);
    }, new VelocityTemplateEngine());
  }
}