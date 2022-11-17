/*
 * CS3210 - Principles of Programming Languages - Fall 2022
 * Instructor: Thyago Mota
 * Description: Activity 06 - Storage Binding
 */

/*
A sandwich is defined by a name, number of calories (integer is fine), and price. Users should be able to create a sandwich given its name, number of calories, and price. If informed number of calories or price is negative, make sure those values are initialized to zero. Define “toString” and a method called “isHealthy” that returns true if the number of calories is less than 250, false otherwise.
 */
public class Sandwich {

    //instance variables - heap dynamic -(location of variables cannot be determined in run time) everytime you run the program the location can be different
    //name: heap-dynamic
    private String name;
    //calories: heap-dynamic
    private int calories;
    //price:heap-dynamic
    private double price;
    //HEALTHY_CALORIES: static
    //before the program runs the location can be determined 
    private static final int HEALTHY_CALORIES = 250;
    
    
    
    //name(parameter): stack dynamic
    //calories (parameter): stack dynamic
    //price (parameter): stack dynamic
    
    //cant be determined before the program starts running 
    
    // Sandwich is a constructor function and in order to call function they are local variables within the function and variables will be created once a sandwhuch is created 
    public Sandwich(String name, int calories, double price) {
        this.name = name;
        if (calories < 0)
            this.calories = 0;
        else
            this.calories = calories;
        if (price < 0)
            this.price = 0;
        else
            this.price = price;
    }

    @Override
    public String toString() {
        //literal string is an object 
        // object rescides in a heap 
        // (implicit) heap-dynamic 
        return "Sandwich{" +
                "name='" + name + '\'' +
                ", calories=" + calories +
                ", price=" + price +
                '}';
    }

    public boolean isHealthy() {
        return calories < HEALTHY_CALORIES;
    }
//args: stack-dynamic
    // teh args variable the value is an address but the variable will be in the stack frame
    public static void main(String[] args) {
        // s1: stack-dynamic because its a local variabble 
        // new Sandwich("Big Mac", 450, 5.5) : (explict) heap dynamic
        Sandwich s1 = new Sandwich("Big Mac", 450, 5.5);
        System.out.println(s1);
        System.out.println("Is healthy? " + s1.isHealthy());
    }
}

