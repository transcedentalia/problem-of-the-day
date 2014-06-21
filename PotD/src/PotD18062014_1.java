import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;


public class PotD18062014_1 {

	/*
	 * Complexity: O(n) with constant additional space;
	 */
	
	public static boolean checkUniqV1(String s) {
		
		if(s == null)
			return false;
	
		if(s.length() == 1)
			return true;
		
		Set<Character> stringChars = new HashSet<Character>();
		
		for(int i = 0; i < s.length(); ++i) {
			
			if(stringChars.contains(s.charAt(i)))
				return false;
			
			stringChars.add(s.charAt(i));
		}
		
		return true;
	}
	
	/*
	 * Complexity: O(nlogn) without additional space;
	 */
	public static boolean checkUniqV2(char[] s) {
		
		if(s == null)
			return false;
	
		if(s.length == 1)
			return true;
		
		Arrays.sort(s);
		
		for(int i = 0; i < s.length - 1; ++i)
			if(s[i] == s[i + 1])
				return false;
		
		return true;
	}
	
	public static void main(String[] args) {
		System.out.println(checkUniqV1(null));
		System.out.println(checkUniqV1(""));
		System.out.println(checkUniqV1("a"));
		System.out.println(checkUniqV1("abcdefghi"));
		System.out.println(checkUniqV1("aaaaaaabc"));
		
		System.out.println(checkUniqV2(null));
		System.out.println(checkUniqV2("".toCharArray()));
		System.out.println(checkUniqV2("a".toCharArray()));
		System.out.println(checkUniqV2("abcdefghi".toCharArray()));
		System.out.println(checkUniqV2("aaaaaaabc".toCharArray()));
	}
}
