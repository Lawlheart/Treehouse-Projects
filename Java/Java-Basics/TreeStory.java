import java.io.Console;

public class TreeStory {

	public static void main(String[] args) {
		Console console = System.console();

		// "In the book War of the __nouns__, the main character is an anonymous __job__ who records the arrival of __animals__ in __place__.
		// Needless to say, havoc reigns as the __animals__ continue to __verb__ everything in sight, until they are killed by the common __noun__.\n"

		// String sAge = console.readLine("How old are you?  ");
		// int age = Integer.parseInt(sAge);
		// if(age < 13) {
		// 	console.printf("Sorry, you must be at least 13 to use this program.\n");
		// 	System.exit(0);
		// }

		String noun;
		boolean invalid;
		do {
			noun = console.readLine("Enter a noun. ");
			invalid = noun.equalsIgnoreCase("dork");
			if(invalid) {
				console.printf("bad word, try again. ");
			}
		} while(invalid);
		String job = console.readLine("Enter a job. ");
		String animals = console.readLine("Enter an animal(plural). ");
		String place = console.readLine("Enter a place. ");
		String verb = console.readLine("Enter a verb. ");

		
		console.printf("In the book War of the %s, the main character is an anonymous %s who records the arrival of %s in %s.\n", animals, job, animals, place);
		console.printf("Needless to say, havoc reigns as the %s continue to %s everything in sight, until they are killed by the common %s.\n", animals, verb, noun);
	}

}