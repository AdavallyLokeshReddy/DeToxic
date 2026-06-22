import java.util.Scanner;
import java.util.Arrays;



public class ReverseArray {
public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("enter the size of the array");
    int size = sc.nextInt();

    int[] arr = new int[size];
    System.out.println("enter the elements of the array");

    for (int i = 0; i < size; i++) {
        arr[i] = sc.nextInt();
    }

    System.out.println("Original Array: " + Arrays.toString(arr));

    // Reverse the array
    for (int i = 0; i < size / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[size - 1 - i];
        arr[size - 1 - i] = temp;
    }
         int start = 0;
        int end = size - 1;
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }


    System.out.println("Reversed Array: " + Arrays.toString(arr));
}    
}
