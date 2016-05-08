import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

import spark.ModelAndView;
import spark.template.velocity.VelocityTemplateEngine;
import static spark.Spark.*;

import app.Treet;
import app.Treets;

public class App {
  public static void main(String[] args) {
    staticFileLocation("/public");
    String layout = "templates/layout.vtl";

    Treet[] treets = Treets.load();

    Set<String> allHashTags = new HashSet<String>();
    Set<String> allMentions = new TreeSet<String>();
    for(Treet treet : treets) {
      allHashTags.addAll(treet.getHashTags());
      allMentions.addAll(treet.getMentions());
    }

    Map<String, Integer> hashTagCounts = new HashMap<String, Integer>();
    Map<String, Integer> mentionCounts = new TreeMap<String, Integer>();
    for(Treet treet : treets) {
      for(String tag : treet.getHashTags()) {
        Integer count = hashTagCounts.get(tag);
        if(count == null) {
          count = 0;
        }
        count ++;
        hashTagCounts.put(tag, count);
      }
      for(String mention : treet.getMentions()) {
        Integer count = mentionCounts.get(mention);
        if(count == null) {
          count = 0;
        }
        count ++;
        mentionCounts.put(mention, count);
      }
    }

    Map<String, List<Treet>> treetsByAuthor = new HashMap<String, List<Treet>>();
    for(Treet treet : treets) {
      List<Treet> authoredTreets = treetsByAuthor.get(treet.getAuthor());
      if(authoredTreets == null) {
        authoredTreets = new ArrayList<Treet>();
        treetsByAuthor.put(treet.getAuthor(), authoredTreets);
      }
      authoredTreets.add(treet);
    }

    get("/", (request, response) -> {
      Map<String, Object> model = new HashMap<String, Object>();
      model.put("template", "templates/index.vtl");
      model.put("treets", treets);
      model.put("hashtags", allHashTags);
      model.put("mentions", allMentions);
      model.put("tagCounts", hashTagCounts);
      model.put("mentionCounts", mentionCounts);
      return new ModelAndView(model, layout);
    }, new VelocityTemplateEngine());
    
    get("/:author", (request, response) -> {
      Map<String, Object> model = new HashMap<String, Object>();
      model.put("template", "templates/author.vtl");
      model.put("author", request.params(":author"));
      model.put("treets", treetsByAuthor.get(request.params(":author")));
      return new ModelAndView(model, layout);
    }, new VelocityTemplateEngine());
  }
}
