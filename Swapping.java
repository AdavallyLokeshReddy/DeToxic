public class Swapping {
int A = 10;
int B = 20;

public static void main(String []args) {
    //without using a temporary variable
    A = A + B ;
    B = B - A;
    A = A - B;
     
    System.out.println("After swapping: A = " + A, "B = " + B);
}
}
