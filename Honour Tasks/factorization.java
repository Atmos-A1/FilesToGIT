import java.util.Scanner;

public class factorization{
	public static void main(String[]args){

		Scanner userInput = new Scanner(System.in);

		System.out.print("Enter a positive number: ");

		int number = userInput.nextInt();

		int factor = 2;

		int sum = 0;

		int product = 1;

		while(number > 1){
			if(number % factor == 0){
				System.out.println(factor + " ");
				
				product *= factor;

				sum += factor;

				number /= factor;
			}
			else{
				factor++;
			}
		}
		System.out.println("The sum of factors is: " + sum);

		System.out.println("The product of the factors is: " + product);

	}
}