
public class PotD19062014_1 {

	public static StringBuffer reverseString(StringBuffer s) {
		
		char temp;
		
		if(s == null) 
			return null;
		
		for(int i = 0; i < s.length() / 2; ++i) {
			temp = s.charAt(i);
			s.setCharAt(i, s.charAt(s.length() - i - 1));
			s.setCharAt(s.length() - i - 1, temp);
		}
		
		return s;
	}
	
	public static void main(String[] args) {
		System.out.println(reverseString(null));
		System.out.println(reverseString(new StringBuffer("")));
		System.out.println(reverseString(new StringBuffer("abcd")));
		System.out.println(reverseString(new StringBuffer("abcde")));

	}

}
