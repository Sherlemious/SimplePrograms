/*Hi, I am Jen, this is a simple calculator using java*/
import java.util.Scanner;
class Operation{
	private int a,b;
	public void getData(){
		Scanner value = new Scanner(System.in);
		System.out.print("Enter first number :");
		a = value.nextInt();
		System.out.print("Enter second number :");
		b = value.nextInt();
	}
	public void sum(){
		int s = a+b;
		System.out.println("Sum of these numbers = "+ s);
	}
	public void diff(){
		int s = a-b;
		System.out.println("Difference of these numbers = "+ s);
	}
	public void product(){
		int s = a*b;
		System.out.println("Product of these numbers = "+ s);
	}
	public void quotient(){
		int s = a/b;
		System.out.print("Quotient of these numbers = "+ s);
	}
}

public class Calculator{
	public static void main(String args[]){
		Operation a = new Operation();
		a.getData();
		a.sum();
		a.diff();
		a.product();
		a.quotient();
	}
}