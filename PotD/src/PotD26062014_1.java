import java.util.HashSet;
import java.util.Set;


public class PotD26062014_1 {

	public static Node removeDuplicate(Node head) {
		
		if(head == null || head.next == null)
			return head;
		
		Set<Integer> uniqValues = new HashSet<Integer>();
		uniqValues.add(head.data);
		
		Node n = head;
		while(n != null) {
			if(n.next != null) {
				if(uniqValues.contains(n.next.data)){
					n.next = n.next.next;
				}
				else {
					uniqValues.add(n.next.data);
					n = n.next;
				}
			}
			else {
				break;
			}
		}
		
		return head;
		
	}
	
	public static Node sumLists(Node n1, Node n2) {
		
		if(n1 == null || n2 == null)
			return null;
		
		Node sum = null;
		int sumTemp  = 0, transport = 0;
		while(n1 != null && n2 != null) {
			int temp = n1.data + n2.data;
			Node newNode = new Node((temp % 10) + transport);
			transport = temp / 10;
			
			if(sum == null)
				sum = newNode;
			else {
				newNode.next = sum;
				sum = newNode;
			}
			
			n1 = n1.next;
			n2 = n2.next;
		}
		
		if(transport != 0) {
			Node head = new Node(transport);
			head.next = sum;
			sum = head;
		}
		
		return sum;
	}
	
	public static Node getStartLoopNode(Node n) {
		
		if(n == null)
			return null;
		
		Set<Integer> uniqValues = new HashSet<Integer>();
		
		while(n != null) {
			if(uniqValues.contains(n.data)) {
				return n;
			}
			
			uniqValues.add(n.data);
			n = n.next;
		}
		
		return null;
		
	}
	
	public static void main(String[] args) {
		/*Node head = null;

		for(int i = 0; i < 10; ++i) {
			head = PotD24062014_1.addNodeRear(head, i);
			head = PotD24062014_1.addNodeRear(head, 1);
		}
		Node head1 = new Node(3);
		head1 = PotD24062014_1.addNodeRear(head1, 1);
		head1 = PotD24062014_1.addNodeRear(head1, 5);
		PotD24062014_1.printList(head1);
		
		Node head2 = new Node(6);
		head2 = PotD24062014_1.addNodeRear(head2, 9);
		head2 = PotD24062014_1.addNodeRear(head2, 2);
		PotD24062014_1.printList(head2);

		//head = removeDuplicate(head);
		Node head = sumLists(head1, head2);
		PotD24062014_1.printList(head);
		*/
		
		Node head1 = new Node(1);
		PotD24062014_1.addNodeRearReturnNode(head1, 2, null);
		Node loopHead = PotD24062014_1.addNodeRearReturnNode(head1, 3, null);
		PotD24062014_1.addNodeRearReturnNode(head1, 4, null);
		PotD24062014_1.addNodeRearReturnNode(head1, 5, null);
		PotD24062014_1.addNodeRearReturnNode(head1, 6, loopHead);
		
		System.out.println(getStartLoopNode(head1).data);
		

	}

}
