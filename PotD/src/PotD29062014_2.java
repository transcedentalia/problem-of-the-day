
public class PotD29062014_2 {

	static class MyQueue{
		public Stack a;
		public Stack b;
		
		public MyQueue() {
			 a = new Stack();
			 b = new Stack();
		}
		
		public void enqueue(Node n) {
			if(a.isEmpty() == true && b.isEmpty() == true ||
			   a.isEmpty() == false && b.isEmpty() == true) {
				
				a.push(n);
				return;
			}
			
			if(a.isEmpty() == true && b.isEmpty() == false) {
				
				while(b.isEmpty() == false) {
					a.push(b.pop());
				}
				
				a.push(n);
			}
		}
		
		public Node dequeue() {
			
			if(a.isEmpty() == true && b.isEmpty() == true) {
				return null;
			}
			
			if(a.isEmpty() == true && b.isEmpty() == false) {
				return b.pop();
			}
			
			if(a.isEmpty() == false && b.isEmpty() == true) {
				while(a.isEmpty() == false) {
					b.push(a.pop());
				}
				return b.pop();
			}
			
			return null;
		}
	}
	
	public static void main(String[] args) {
		
		MyQueue q = new MyQueue();
		
		for(int i = 0; i < 5; ++i) {
			q.enqueue(new Node(i));
		}
		
		for(int i = 0; i < 5; ++i) {
			System.out.print(q.dequeue().data + " ");
		}
	}
}
