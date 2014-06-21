
public class PotD20062014_2 {

	public static boolean arePalindroms(String s1, String s2) {
	
		if(s1 == null || s2 == null)
			return false;
		
		if(s1.length() != s2.length())
			return false;
		
		for(int i = 0 ; i < s1.length(); ++i)
			if(s1.charAt(i) != s2.charAt(s2.length() - i - 1))
				return false;
		
		return true;
	}
	
	public static boolean areAnagrams(String s1, String s2) {
		
		if(s1 == null || s2 == null)
			return false;
		
		if(s1.length() != s2.length())
			return false;
		
		int[] freq1 = new int[256];
		int[] freq2 = new int[256];
		
		for(int i = 0; i < s1.length(); ++i) {
			
			freq1[(int)s1.charAt(i)] ++;
			freq2[(int)s2.charAt(i)] ++;
			
		}
		
		for(int i = 0; i < freq1.length; ++i) {
			if(freq1[i] != freq2[i]) 
				return false;
		}
		
		return true;
		
	}
	
	public static void main(String[] args) {
		System.out.println(arePalindroms("ana", null));
		System.out.println(arePalindroms("aa", "bbbb"));
		System.out.println(arePalindroms("ana", "ara"));
		System.out.println(arePalindroms("hhh", "ara"));
		
		System.out.println(areAnagrams("ana", null));
		System.out.println(areAnagrams("aaaa", "bbb"));
		System.out.println(areAnagrams("ORIENTALISTA", "IMPERTINENTA"));
		System.out.println(areAnagrams("ORIENTALISTA", "RATIONALISTE"));

	}

}
