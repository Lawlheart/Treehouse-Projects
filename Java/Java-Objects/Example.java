public class Example {
  public static void main(String[] args) {
    System.out.println("We are making a new Pez Dispenser.");
    PezDispenser dispenser = new PezDispenser("Yoda");
    System.out.printf("The dispenser character is %s\n", dispenser.getCharacterName());

    System.out.println("Loaded Dispenser");
    try {
      dispenser.load(400);
    } catch(IllegalArgumentException ex) {
      System.out.println("Whoa there!");
      System.out.printf("The error was: %s\n", ex.getMessage());
    }

    while(dispenser.dispense()) {
      System.out.printf("Chomp! (%s left)\n", dispenser.getPezCount());
    }

    if(dispenser.isEmpty()) {
      System.out.println("Ate all the pez!");
    }
  }
}