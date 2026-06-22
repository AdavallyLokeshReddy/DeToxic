// Abstraction: Abstract class
abstract class Animal {
    private String name; // Encapsulation: private field

    // Constructor
    public Animal(String name) {
        this.name = name;
    }

    // Getter (Encapsulation)
    public String getName() {
        return name;
    }

    // Abstract method (must be implemented by subclasses)
    public abstract void sound();

    // Normal method
    public void sleep() {
        System.out.println(name + " is sleeping...");
    }
}

// Inheritance: Dog inherits from Animal
class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }

    // Overriding: redefining sound() method
    @Override
    public void sound() {
        System.out.println(getName() + " says: Woof Woof!");
    }

    // Overloading: same method name, different parameters
    public void sound(int times) {
        for (int i = 0; i < times; i++) {
            System.out.println(getName() + " says: Woof!");
        }
    }
}

// Another subclass
class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }

    @Override
    public void sound() {
        System.out.println(getName() + " says: Meow!");
    }
}

// Main class to test everything
public class OOPDemo {
    public static void main(String[] args) {
        // Polymorphism: parent reference, child object
        Animal dog = new Dog("Buddy");
        Animal cat = new Cat("Kitty");

        dog.sound();   // Runtime polymorphism (overriding)
        cat.sound();

        dog.sleep();
        cat.sleep();

        // Method overloading
        Dog d = new Dog("Rocky");
        d.sound();        // Single bark
        d.sound(3);       // Bark 3 times
    }
}