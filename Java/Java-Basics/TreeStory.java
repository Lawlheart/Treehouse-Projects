import java.io.Console;

public class TreeStory {

	public static void main(String[] args) {
		Console console = System.console();

		// "In the book War of the __nouns__, the main character is an anonymous __job__ who records the arrival of __animals__ in __place__.
		// Needless to say, havoc reigns as the __animals__ continue to __verb__ everything in sight, until they are killed by the common __noun__.\n"

		String nouns = console.readLine("Enter a noun(plural)."); 
		String job = console.readLine("Enter a job.");
		String animals = console.readLine("Enter an animal(plural).");
		String place = console.readLine("Enter a place.");
		String verb = console.readLine("Enter a verb.");
		String noun = console.readLine("Enter a noun.");

		
		console.printf("In the book War of the %s, the main character is an anonymous %s who records the arrival of %s in %s.\n", nouns, job, animals, place);
		console.printf("Needless to say, havoc reigns as the %s continue to %s everything in sight, until they are killed by the common %s.\n", animals, verb, noun);
	}

}