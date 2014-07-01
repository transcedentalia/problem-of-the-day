
public class PotD29062014_1 {
	
	public static void main(String[] args) {
		Stack myStack = new Stack();
		
		myStack.push(new Node(3));
		myStack.push(new Node(1));
		myStack.push(new Node(5));
		myStack.push(new Node(2));
		
		myStack.printStack();
		System.out.println(myStack.min());
		System.out.println(myStack.pop().data);
		myStack.printStack();
		
	}

}
