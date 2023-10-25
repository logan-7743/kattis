import java.io.BufferedReader;
import java.io.*;
import java.util.*;

public class Lab82 {
    public static void main(String[] args) throws IOException {
        // Create a BufferedReader to read input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // Create a TreeMap to store strings and their counts
        TreeMap<String, Integer> tree = new TreeMap<>();
        
        String s = br.readLine();
        int count = 0;

        // Read input until null is encountered
        while (s != null) {
            count++;
            // Add the string to the TreeMap, incrementing its count
            tree.put(s, tree.getOrDefault(s, 0) + 1);
            s = br.readLine();
        }

        // Create a BufferedWriter to write output
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // Calculate and write the relative frequency of each string
        for (String x : tree.keySet()) {
            double frequency = tree.get(x) * 100.0 / count;
            bw.write(x + " " + frequency + "\n");
        }

        // Close the BufferedWriter
        bw.close();
    }
}
