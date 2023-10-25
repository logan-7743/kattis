import java.util.*;

public class Triple_Texting {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String text = sc.nextLine();  // Read the input text
        
        // Split the input text into three equal parts
        String text1 = text.substring(0, text.length() / 3);
        String text2 = text.substring(text.length() / 3, text.length() / 3 * 2);
        String text3 = text.substring(text.length() / 3 * 2, text.length());
        
        // Check if at least two of the three parts are the same
        if (text1.equals(text2)) {
            System.out.println(text1);
        } else if (text1.equals(text3)) {
            System.out.println(text1);
        } else if (text2.equals(text3)) {
            System.out.println(text2);
        }
    }
}
