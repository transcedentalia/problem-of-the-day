public class PotD24062014_1 {
	
	public static Node addNodeRearReturnNode(Node head, int data, Node nextNode) {
		if(head == null)
			return new Node(data);

		Node n = head;
		while(n.next != null)
			n = n.next;
		
		Node newNode = new Node(data, nextNode);
		n.next = newNode;

		return newNode;
	}

	public static Node addNodeRear(Node head, int data) {
		if(head == null)
			return new Node(data);

		Node n = head;
		while(n.next != null)
			n = n.next;

		n.next = new Node(data);

		return head;
	}

	public static Node addNodeFront(Node head, int data) {
		if(head == null)
			return new Node(data);

		Node temp = new Node(data);
		temp.next = head;
		head = temp;

		return head;
	}

	public static Node deleteNodeV1(Node n, int data) {
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

	public static Node deleteNodeV2(Node n, int data) {
		if(n == null)
			return null;

		Node head = n;
		while(n != null) {
			if(n.data == data) {
				if(n.next != null) {
					n.data = n.next.data;
					n.next = n.next.next;
				}
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
			head = addNodeRear(head, i);
		}
		printList(head);

		//head = reverseList(head);
		head = deleteNodeV1(head, 4);

		printList(head);
	}

}