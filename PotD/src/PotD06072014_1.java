import java.util.Stack;

public class PotD06072014_1 {

	public static void preorder(Node root) {
		
		if(root == null) {
			return;
		}
		
		Stack<Node> st = new Stack<Node>();
		st.push(root);
		
		while(st.isEmpty() == false) {
			Node temp = st.pop();
			System.out.print(temp.data + " ");
			
			if(temp.right != null) {
				st.push(temp.right);
			}
			
			if(temp.left != null) {
				st.push(temp.left);
			}
				
		}
		
	}
	
	public static void inorder(Node root) {
		
		if(root == null) {
			return;
		}
		
		Node current = root;
		Stack<Node> st = new Stack<Node>();
		
		while(current != null || st.isEmpty() == false) {
			
			if(current != null) {
				st.push(current);
				current = current.left;
			}
			else {
				Node temp = st.pop();
				System.out.print(temp.data + " ");
				current = temp.right;
			}
			
		}
	}
	
	public static void postorder(Node root) {
		
		if(root == null) {
			return;
		}
		
		Stack<Node> s1 = new Stack<Node>();
		Stack<Node> s2 = new Stack<Node>();
		
		s1.push(root);
		while(s1.isEmpty() == false) {
			Node temp  = s1.pop();
			s2.push(temp);
			
			if(temp.left != null) {
				s1.push(temp.left);
			}
			
			if(temp.right != null) {
				s1.push(temp.right);
			}
			
		}
		
		while(s2.isEmpty() == false) {
			System.out.print(s2.pop().data + " ");
		}
	}
	
	public static void main(String[] args) {
		
		Node root = new Node(1,
						new Node(2,
								new Node(4, null, null),
								new Node(5, null, null)),
						new Node(3,
								null,
								new Node(6,
									new Node(7,
										new Node(8, null, null),
										null),
									null)));
		preorder(root);
		System.out.println();
		inorder(root);
		System.out.println();
		postorder(root);

	}

}
