public class AccessModifiers {
    public static void main(String[] args) {

        AccessModifiers obj = new AccessModifiers();
        
        obj.publicMethod();
    }
        
        
    
    public void publicMethod() {
        System.out.println("This is a public method.");
    }
    
    private void privateMethod() {
        System.out.println("This is a private method.");
    }
    
    protected void protectedMethod() {
        System.out.println("This is a protected method.");
    }
}
