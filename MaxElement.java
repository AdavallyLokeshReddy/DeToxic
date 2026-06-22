import java.util.Scanner;
import java.util.Arrays;


public class MaxElement {
    public static void main(String []args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("enter the size of the array");
    int size = sc.nextInt();

    int[] arr = new int [size];
    System.out.println("enter the elements");

    for (int i = 0; i < size; i++) {
        arr[i] = sc.nextInt();

    }

    int max = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > max) {
            max = arr[i];

        }
    }


    System.out.println("max element: " + max);
} 
}
