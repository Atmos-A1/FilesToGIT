import java.util.Scanner;

public class Kata1{
	public static int add(int num1, int num2){
		int sum = num1 + num2;
		return sum;
	}

	public int subtract(int num1, int num2){
		int difference = num1 - num2;
		return difference;

	}

	public boolean oddNumber(Scanner input){

		System.out.println("Enter a number: ");
		int number1= input.nextInt();
		int number = collectInput(number1);
		if (number % 2 != 0) return true;
		return false;

	}



	public int collectInput(int input){

		while(input <= 0){
			System.out.println("Number cannot be less than 0:");
			System.out.print("Enter number again: ");
			input = new Scanner(System.in).nextInt();
		}
		
		return input;
		
	}
	// Scanner input = new Scanner(System.in);
	// oddNumber()
}

// if(number1 % 2 != 0){
// 			return true;
// 			}
// 			else{
// 				System.out.println("Enter a number greater than zero: ");
// 				return false;
// 			}