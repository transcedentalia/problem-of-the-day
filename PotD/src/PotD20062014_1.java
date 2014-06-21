import java.util.ArrayList;
import java.util.Arrays;


public class PotD20062014_1 {

	public static char[] removeDuplicate(char[] s) {
		if(s == null)
			return null;
		
		if(s.length == 1)
			return s;
		
		for(int i = 0 ; i < s.length - 1; ++i) {
			int j = i + 1;
			
			while(j < s.length) {
				
				if(s[i] == s[j]) {
					
					for(int k = j; k < s.length - 1; ++k){
						s[k] = s[k + 1];
					}
					s = Arrays.copyOf(s, s.length - 1);
				}
				else {
					++j;
				}
			}
		}
		
		return s;
	}
	
	public static void printArray(char[] s) {
		for(int i = 0; i < s.length; ++i)
			System.out.print(s[i]);
	}
	
	public static void main(String[] args) {
		printArray(removeDuplicate("ff".toCharArray()));

	}

}
