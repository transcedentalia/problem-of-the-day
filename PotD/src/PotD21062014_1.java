import java.util.ArrayList;
import java.util.Arrays;


public class PotD21062014_1 {

	public static ArrayList<Character> replaceSpaces(ArrayList<Character> s) {
		if(s == null || s.size() == 0)
			return null;
		
		int extendCount = 0;
		for(int i = 0; i < s.size(); ++i)
			if(s.get(i) == ' ')
				extendCount += 2;
		
		if(extendCount == 0)
			return s;
		
		int pos = s.size();
		int oldEnd = s.size() - 1;
		while(extendCount > 0) {
			s.add(' ');
			extendCount --;
		}
		
		int newEnd = s.size() - 1;
		while(oldEnd >= 0) {
			if(s.get(oldEnd) == ' ') {
				s.set(newEnd --, '0');
				s.set(newEnd --, '2');
				s.set(newEnd --, '%');
			}
			else {
				s.set(newEnd --, s.get(oldEnd));
			}
			
			oldEnd --;
		}
		
		return s;
		
	}
	
	public static void printArray(ArrayList<Character> s) {
		
		if(s == null)
			return;
		
		for(int i = 0; i < s.size(); ++i)
			System.out.print(s.get(i));
		
		System.out.println();
	}
	
	public static ArrayList<Character> buildArrayList(String s) {
		ArrayList<Character> result = new ArrayList<Character>();
		
		for(int i = 0; i < s.length(); ++i)
			result.add(s.charAt(i));
		
		return result;
	}


	public static void main(String[] args) {
		printArray(replaceSpaces(null));
		printArray(replaceSpaces(buildArrayList("")));
		printArray(replaceSpaces(buildArrayList("abc")));
		printArray(replaceSpaces(buildArrayList("a b c    ")));

	}

}
