import java.util.*;

public class SecureDoors {
    public static void main(String[] args) {
        // Create a HashSet to store the names of individuals inside the building
        HashSet<String> hash = new HashSet<>();
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();  // Read the number of actions
        
        for (int i = 0; i < n; i++) {
            String curr = sc.next();  // Read the action (entry or exit)
            String name = sc.next();  // Read the name of the individual
            
            if (curr.equals("entry") && hash.contains(name)) {
                // Anomaly: The individual entered when they were already inside
                System.out.println(name + " entered (ANOMALY)");
            } else if (curr.equals("exit") && !hash.contains(name)) {
                // Anomaly: The individual exited when they were not inside
                System.out.println(name + " exited (ANOMALY)");
            } else if (curr.equals("entry") && !hash.contains(name)) {
                // Record the entry and add the individual to the building
                System.out.println(name + " entered");
                hash.add(name);
            } else if (curr.equals("exit") && hash.contains(name)) {
                // Record the exit and remove the individual from the building
                System.out.println(name + " exited");
                hash.remove(name);
            } else {
                System.out.println("broke");  // Invalid input, something went wrong
            }
        }
    }
}
