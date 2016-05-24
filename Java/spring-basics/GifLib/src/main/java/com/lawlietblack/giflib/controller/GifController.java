package com.lawlietblack.giflib.controller;

import com.lawlietblack.giflib.data.GifRepository;
import com.lawlietblack.giflib.model.Gif;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import java.time.LocalDate;
import java.util.List;

@Controller
public class GifController {
    @Autowired
    private GifRepository gifRepository;

    @RequestMapping("/")
    public String listGifs(ModelMap modelMap) {
        List<Gif> allGifs = gifRepository.getAllGifs();
        modelMap.put("gifs", allGifs);
        return "home";
    }

    @RequestMapping("/gif/{name}")
    public String gifDetails(@PathVariable String name, ModelMap modelMap) {
        Gif gif = gifRepository.findByName(name);
        modelMap.put("gif", gif);
        return "gif-details";
    }

    //TODO:krb add a controller method that intercepts /favorites, grabs the list of Gif objects from your new repository method, and adds it to the ModelMap.
    //TODO:krb add a favorites view
    //TODO:krb add a search method
    /*
        Then, you must have a controller method that intercepts the URI specified by the search form's action attribute.
        This method must have a parameter annotated with @RequestParam that is named the same as the name attribute of
        the text input in the search form. This is similar to our use of @PathVariable, except that the search term will
        appear in the URI's query string, for example /search?q=compiler. In this method, you'll also call the repository
        method you created for searching a Gif object's name field.
     */
    //TODO:krb add a search view
}
