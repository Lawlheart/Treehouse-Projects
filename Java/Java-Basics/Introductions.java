import java.io.Console;
 
public class Introductions {
  
    public static void main(String[] args) {
        Console console = System.console();
        // Welcome to the Introductions program!  Your code goes below here
        String firstName = "Neko";
        console.printf("Hello World!\n");
        console.printf("%s is learning Java!\n", firstName);
  }
}