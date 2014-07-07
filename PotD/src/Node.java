public class Node{
	
	public int data;
	public Node next;
	
	public Node parent;
	public Node left;
	public Node right;
	
	public Node(int data) {
		this.data = data;
		this.next = null;
	}
	
	public Node(int data, Node next) {
		this.data = data;
		this.next = next;
	}
	
	public Node(int data, Node left, Node right) {
		this.data = data;
		this.left = left;
		this.right = right;
		this.parent = null;
	}
}