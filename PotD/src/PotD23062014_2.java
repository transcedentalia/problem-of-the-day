
public class PotD23062014_2 {
	
	public static boolean isRotation(String s1, String s2) {
		
		if(s1 == null || s2 == null)
			return false;
		
		String s1Concat = s1+s1;
		if(s1Concat.contains(s2))
			return true;
		
		return false;
	}
	
	public static void main(String[] args) {
		System.out.println(isRotation("erwatt", "watter"));
	}

}
