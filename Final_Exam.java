import java.util.*;

public class finalexam2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();  // Read the number of answers
        ArrayList<String> arr = new ArrayList<>();  // Create an ArrayList to store answers
        
        // Read and store the answers in the ArrayList
        for (int i = 0; i < n; i++) {
            arr.add(sc.next());
        }
        
        int correct = 0;  // Initialize a variable to count correct answers
        
        // Iterate through the answers and count the correct ones
        for (int i = 0; i < arr.size() - 1; i++) {
            if (arr.get(i).equals(arr.get(i + 1))) {
                correct++;
            }
        }
        
        System.out.println(correct);  // Print the count of correct answers
        sc.close();  // Close the scanner
    }
}
