import java.util.Scanner;

public class StringExample2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a string:");
        String inputString = sc.nextLine();

        String result = ""; // start with an empty string

        // iterate through each character of the input string
        for (int i = 0; i < inputString.length(); i++) {
            char ch = inputString.charAt(i);

            // if character is 'e', replace with 'a'
            if (ch == 'e') {
                result += 'a';
            } else {
                result += ch;
            }
        }

        System.out.println("The modified string is: " + result);
    }
}