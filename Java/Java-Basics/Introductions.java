import java.io.Console;
 
public class Introductions {
  
    public static void main(String[] args) {
        Console console = System.console();
        // Welcome to the Introductions program!  Your code goes below here
        String firstName = console.readLine("WHAT ... is your NAME?  ");
        console.printf("Hello World!\n");
        console.printf("%s is learning Java!\n", firstName);
        System.out.printf("Good job, m%d%n", 8);
  }
}