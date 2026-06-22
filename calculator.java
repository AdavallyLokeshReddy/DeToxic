import java.util.Scanner;

public class Calculator {

    // Separate methods for each operation
    public static double add(double a, double b) {
        return a + b;
    }

    public static double subtract(double a, double b) {
        return a - b;
    }

    public static double multiply(double a, double b) {
        return a * b;
    }

    public static double divide(double a, double b) {
        if (b != 0) {
            return a / b;
        } else {
            System.out.println("Error: Division by zero!");
            return Double.NaN;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first number: ");
        double num1 = sc.nextDouble();

        System.out.print("Enter second number: ");
        double num2 = sc.nextDouble();

        System.out.print("Enter operator (+, -, *, /): ");
        char operator = sc.next().charAt(0);

        double result = 0;

        if (operator == '+') {
            result = add(num1, num2);
        } else if (operator == '-') {
            result = subtract(num1, num2);
        } else if (operator == '*') {
            result = multiply(num1, num2);
        } else if (operator == '/') {
            result = divide(num1, num2);
        } else {
            System.out.println("Invalid operator!");
        }

        System.out.println("Result: " + result);

        sc.close();
    }
}