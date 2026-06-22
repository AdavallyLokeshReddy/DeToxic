import java.util.Scanner;
import java.util.Arrays;


public class LinearSearch {
    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the size of the array");
        int size = sc.nextInt();

        int[] arr = new int[size];
        System.out.println("enter the elements of the array");

        for (int i = 0; i < size; i++) {
            arr[i] = sc.nextInt();
        }

        System.out.println("enter the element to search");
        int target = sc.nextInt();

        boolean found = false;
        for (int i = 0; i < size; i++) {
            if (arr[i] == target) {
                found = true;
                break;
            }
        }

        if (found) {
            System.out.println("Element found in the array.");
        } else {
            System.out.println("Element not found in the array.");
        }

        sc.close();
    }
}
