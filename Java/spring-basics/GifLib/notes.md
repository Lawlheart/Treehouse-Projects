
### Spring Server Process

1. user makes HTTP request to our Web Server (Tomcat)
2. Based on the request, the server knows to pass the request to our app
3. In our app, a dispatcher servlet receives the request and examines the URI
4. From the URI, the dispatcher determines which controller and method is being requested using @RequestMapping annot.
5. The mapped controller method is called, which runs our code
6. That data is then fed to a Spring View Resolver. In our case, it will recognize our Thymeleaf templating engine.
7. the view resolver inputs our data into our Thymeleaf template, producing our final HTML product
8. The final product is then passed back to the dispatcher, and then back to the server to create a HTTP response.
9. The server then sends an HTTP response with a 200 status code and our final HTML page.

### Thymeleaf

- XML Compliant, NEED to close <tags/>
- import static files by giving a th: namespace:

    `<link rel="stylesheet" th:href="@{/app.css}">`

- register the namespace with an addition to the html tag:

    `<html lang="en" xmlns:th="http://www.thymeleaf.org">`

- Standard Expressions in Thymeleaf: string literals with variable expression sandwiched

    `<img th:src="@{'/gifs/' + ${gif.name} + '.gif'}" alt="gif" />`

    note: ASSUMES there will get a getName method! Will get an error if not.

### Spring

- Dependency Injection in Spring: add @Autowired to components we want to initialize if we need them
    ```
    @Controller
    public class GifController {
        @Autowired
        private GifRepository gifRepository;
    //... }
    ```
- and add @Component to those classes so @ComponentScan knows how to find them
    ```
    @Component
    public class GifRepository { ... }
    ```
- Path Variables in Spring: add {variableName} to ReqestMapping and @PathVariable to method params
    ```
    @RequestMapping("/gif/{name}")
    public String gifDetails(@PathVariable String name, ModelMap modelMap) { ... }

    ```
