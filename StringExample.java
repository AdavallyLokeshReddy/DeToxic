/*take an array of strings input from the user and find the cumulative length of the strings and print the result.
*/
import java.util.Scanner;
public class StringExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of strings:");
        int n = scanner.nextInt();
        scanner.nextLine();

        String[] strings = new String[n];
        System.out.println("Enter the strings:");
        for (int i = 0; i < n; i++) {
            strings[i] = scanner.nextLine();
        }

        int cumulativeLength = 0;
        for (String str : strings) {
            cumulativeLength += str.length();
        }

        System.out.println("The cumulative length of the strings is: " + cumulativeLength);
    }
}