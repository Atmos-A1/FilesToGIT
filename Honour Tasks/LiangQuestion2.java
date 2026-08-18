import java.util.Arrays;

public class LiangQuestion2{

public static int[] reverseOfArray(int[] numbers){
	int [] reverseArray = new int[numbers.length];
	
	for(int index = 0; index< numbers.length; index++){
		reverseArray[index]  = numbers[numbers.length - 1 - index];
	}
	
	return reverseArray;
	}
	
	public static void main(String[] args) {
			int[] array = {1 , 2 , 3 , 4 , 5};
			System.out.println(Arrays.toString(reverseOfArray(array)));
	}
}


