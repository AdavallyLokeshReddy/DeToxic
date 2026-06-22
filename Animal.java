public class Animal {
    void run() {
        System.out.println("Animal is running");
    }

}
class dog extends Animal {
    void run() {
        System.out.println("Dog is running");
    }
    public static void main(String[] args) {
        dog d = new dog();
        d.run();
    }
}
