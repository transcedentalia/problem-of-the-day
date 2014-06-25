
public class PotD25062014_1 {

	public static Node getKthFromEnd(Node head, int k) {
		
		Node temp = head;
		
		while(k >= 1) {
			if(temp.next != null) {
				temp = temp.next;
				--k;
			}
			else {
				return null;
			}
		}
		
		while(temp != null){
			head = head.next;
			temp = temp.next;
		}
		
		return head;
		
	}
	
	public static Node getMiddleElement(Node head) {
		
		if(head == null)
			return null;
		
		if(head.next == null || head.next.next == null)
			return head;
		
		Node temp = head;
		while(temp != null) {
			if(temp.next != null) {
				temp = temp.next.next;
				head = head.next;
			}else {
				break;
			}
		}
		
		return head;
	}
	
	public static Node removeMiddleElement(Node head) {
		if(head == null || head.next == null)
			return head;
		
		if(head.next.next == null) {
			head = head.next;
			return head;
		}
		
		Node temp = head;
		Node temp2 = head;
		while(temp2 != null) {
			if(temp2.next != null) {
				temp2 = temp2.next.next;
				temp = temp.next;
			}else {
				break;
			}
		}
		
		temp.data = temp.next.data;
		temp.next = temp.next.next;
		
		return head;
		
	}
	
	public static void main(String[] args) {
		Node head = null;
		
		for(int i = 0; i < 11; ++i) {
			head = PotD24062014_1.addNodeRear(head, i);
		}
		PotD24062014_1.printList(head);
		
		System.out.println(getKthFromEnd(head, 6).data);
		head = removeMiddleElement(head);
		PotD24062014_1.printList(head);
		
	}
}
