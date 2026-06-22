import java.util.Scanner;


public class SimpleInterest {
    public static void main(String []args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("enter the principal amount");
        double principal = sc.nextDouble();

        System.out.println("enter rate of interest");
        double rate = sc.nextDouble();

        System.out.println("enter time in years");
        double time = sc.nextDouble();

        double simpleInterest = (principal * rate * time) / 100;
        System.out.println("Simple interest is : " + simpleInterest);
        
        sc.close();
    }
}
