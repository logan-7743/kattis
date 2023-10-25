import java.util.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Read input integers a, b, and c
        int a = sc.nextInt();  // Speed when moving forward
        int b = sc.nextInt();  // Speed when moving backward
        int c = sc.nextInt();  // Destination distance
        
        int distance = 0;  // Initialize the current distance
        int count = 0;     // Initialize the count of steps
        
        while (true) {
            count++;        // Increment the step count
            distance += a;  // Move forward
            
            // If the destination is reached, print the step count and exit the loop
            if (distance >= c) {
                System.out.println(count);
                break;
            }
            
            distance -= b;  // Move backward
        }
    }
}
