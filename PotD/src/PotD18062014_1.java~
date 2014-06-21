import java.util.HashMap;


public class PotD18062014_1 {

	public static boolean checkUniq(String s) {
		
		HashMap<Character, Integer> stringChars = new HashMap<Character, Integer>();
		
		for(int i = 0; i < s.length(); ++i) {
			
			if(stringChars.containsKey(s.charAt(i)))
				return false;
			
			stringChars.put(s.charAt(i), 1);
		}
		
		return true;
	}
	
	public static void main(String[] args) {
		System.out.println(checkUniq(""));
	}
}
