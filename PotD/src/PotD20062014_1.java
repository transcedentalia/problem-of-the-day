import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;


public class PotD20062014_1 {

	/*
	 * Complexity: O(n^3)
	 */
	public static char[] removeDuplicateV1(char[] s) {
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
	
	/*
	 * Complexity: O(n)
	 */
	public static char[] removeDuplicateV2(char[] s) {
		if(s == null)
			return null;
		
		if(s.length == 1)
			return s;
		
		int oldPos = 0, newPos = 0;
		Set<Character> uniqChars = new HashSet<Character>();
		
		while(oldPos < s.length) {
		
			if( !uniqChars.contains(s[oldPos])) {
				uniqChars.add(s[oldPos]);
				s[newPos] = s[oldPos];
				newPos ++;
			}
			
			oldPos ++;
		}
		
		return Arrays.copyOf(s, newPos);

	}
	
	public static void printArray(char[] s) {
		
		if(s == null)
			return;
		
		for(int i = 0; i < s.length; ++i)
			System.out.print(s[i]);
		
		System.out.println();
	}
	
	public static void main(String[] args) {
		printArray(removeDuplicateV1(null));
		printArray(removeDuplicateV1("".toCharArray()));
		printArray(removeDuplicateV1("a".toCharArray()));
		printArray(removeDuplicateV1("aaaaaaaaaaaa".toCharArray()));
		printArray(removeDuplicateV1("abcdefghijklmnop".toCharArray()));
		printArray(removeDuplicateV1("aabbbooojtypppooe".toCharArray()));
		
		printArray(removeDuplicateV2(null));
		printArray(removeDuplicateV2("".toCharArray()));
		printArray(removeDuplicateV2("a".toCharArray()));
		printArray(removeDuplicateV2("aaaaaaaaaaaa".toCharArray()));
		printArray(removeDuplicateV2("abcdefghijklmnop".toCharArray()));
		printArray(removeDuplicateV2("aabbbooojtypppooe".toCharArray()));

	}

}
