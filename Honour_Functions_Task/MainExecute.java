import java.util.Scanner;

public class MainExecute{
/*	public static void main(String[]args){

		Kata1 kata1 = new Kata1();

		Scanner honour = new Scanner(System.in);

		System.out.println("Enter first number: ");
		int number1 = honour.nextInt();

		System.out.println("Enter the second number: ");
		int number2 = honour.nextInt();

		int number3 = kata1.subtract(number1, number2);

		System.out.println(number3);

	}
}
*/


	public static void main(String...args){

		Kata1 honour = new Kata1();

		Scanner rasheed = new Scanner(System.in);

		boolean stateOfNumber = honour.oddNumber(rasheed);

		System.out.println(stateOfNumber);
	}

}