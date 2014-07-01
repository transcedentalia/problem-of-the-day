public class Stack {
		
		public Node stackTop;
		
		public Stack() {
			stackTop = null;
		}
		
		public boolean isEmpty() {
			return (stackTop == null);
		}
		
		public void push(Node n) {
			if(isEmpty() == true) {
				stackTop = n;
				stackTop.min = n.data;
				return;
			}
			
			Node newNode = n;
			newNode.next = stackTop;
			newNode.min = Math.min(stackTop.min, n.data);
			stackTop = newNode;
		}
		
		public Node peek() {
			return stackTop;
		}
		
		public Node pop() {
			if(isEmpty() == true)
				return null;
			
			Node top = stackTop;
			stackTop = stackTop.next;
			
			return top;
		}
		
		public int min() {
			if(isEmpty() == false) {
				return stackTop.min;
			}
			return -1;
		}
		
		public void printStack() {
			Node tempTop = stackTop;
			while(tempTop != null) {
				System.out.print(tempTop.data + " ");
				tempTop = tempTop.next;
			}
			System.out.println();
		}
	}