import java.util.*;

public class Keywords {
    public static void main(String[] args) {
        // Create a HashSet to store unique keywords
        HashSet<String> hash = new HashSet<>();
        
        Scanner sc = new Scanner(System.in);
        
        long n = sc.nextLong();  // Read the number of input lines
        sc.nextLine();  // Consume the newline character
        
        for (long i = 0; i < n; i++) {
            String curr = sc.nextLine().toLowerCase();  // Read and convert the input line to lowercase
            
            // If the input line contains hyphens, replace them with spaces
            if (curr.contains("-")) {
                curr = curr.replace("-", " ");
            }
            
            hash.add(curr);  // Add the current keyword to the HashSet
        }
        
        if (hash.size() > 0) {
            System.out.println(hash.size());  // Print the number of unique keywords
        } else {
            System.out.println(0);  // Print 0 if there are no unique keywords
        }
    }
}
