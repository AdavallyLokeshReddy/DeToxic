import java.util.Scanner;

public class StudentDetails {
    String name;
    int age;
    String address;

    public void getInfo() {
        System.out.println(this.name);
        System.out.println(this.address);
        System.out.println(this.age);

    }
    public static void main(String []args) {
        StudentDetails student = new StudentDetails();
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter name: ");
        student.name = sc.nextLine();

        System.out.println("Enter age: ");
        student.age = sc.nextInt();
        sc.nextLine();
         
        System.out.println("ENter Address: ");
        student.address = sc.nextLine();

        student.getInfo();
    }
}
