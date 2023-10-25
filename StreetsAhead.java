import java.util.*;

public class Week8 {
    public static void main(String[] args) {
        // Create a TreeMap to store streets and their corresponding indices
        TreeMap<String, Integer> tree = new TreeMap<>();
        
        Scanner sc = new Scanner(System.in);
        int streets = sc.nextInt();  // Read the number of streets
        int drivers = sc.nextInt();  // Read the number of drivers
        sc.nextLine();  // Consume the newline character
        
        // Store streets and their indices in the TreeMap
        for (int i = 0; i < streets; i++) {
            tree.put(sc.next(), i + 1);
        }
        
        // Process the drivers and calculate the distances between streets
        for (int i = 0; i < drivers; i++) {
            String first = sc.next();
            String second = sc.next();
            int ans = tree.get(first) - tree.get(second);
            
            // Calculate the absolute difference and subtract 1 to get the distance
            ans = Math.abs(ans) - 1;
            
            System.out.println(ans);  // Print the calculated distance
        }
    }
}
