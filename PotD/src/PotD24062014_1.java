public class PotD24062014_1 {

	public static Node addNode(Node head, int data) {
		if(head == null)
			return new Node(data);
		
		Node n = head;
		while(n.next != null)
			n = n.next;
		
		n.next = new Node(data);
		
		return head;
	}
	
	public static Node deleteNode(Node n, int data) {
		if(n == null)
			return null;
		
		if(n.data == data) {
			n = n.next;
		}
		
		Node head = n;
		while(n.next != null) {
			if(n.next.data == data) {
				n.next = n.next.next;
			}
			else {
				n = n.next;
			}
		}
		return head;
	}
	
	public static Node reverseList(Node head) {
		
		// list null or with one element
		if(head == null)
			return head;
		
		Node prev = null;
		Node current = head;

		while(current != null) {
			Node tmp = current.next;
			current.next = prev;
			prev = current;
			current = tmp;
		}
		
		head = prev;
		
		return head;
		
	}
	
	public static void printList(Node n) {

		while(n != null) {
			System.out.print(n.data + " ");
			n = n.next;
		}
		System.out.println();
	}
	

	public static void main(String[] args) {
		Node head = null;
		
		for(int i = 0; i < 5; ++i) {
			head = addNode(head, i);
		}
		printList(head);
		
		head = reverseList(head);
		head = deleteNode(head, 4);
		
		printList(head);
	}

}
