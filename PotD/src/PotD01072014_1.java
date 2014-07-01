
public class PotD01072014_1 {
	
	public static Node getMin(Node root) {
		
		if(root == null)
			return null;
		
		while(root.left != null){
			root = root.left;
		}
		
		return root;
	}
	
	public static Node getMax(Node root) {
		if(root == null)
			return null;
		
		while(root.right != null){
			root = root.right;
		}
		
		return root;
	}

	public static Node addNodeBST(Node root, Node newNode) {
		if(root == null) {
			root = newNode;
			return root;
		}
		
		if(root.data < newNode.data) {
			root.right = addNodeBST(root.right, newNode);
		}
		
		if(root.data > newNode.data) {
			root.left = addNodeBST(root.left, newNode);
		}
			
		return root;
	}
	
	public static Node deleteNodeBST(Node root, int val)
	{
		if(root.data == val) {
			
			Node temp = root.right;
			while(temp.left != null) {
				temp = temp.left;
			}
			
			root = temp;
			temp = null;
			
			return root;
		}
		
		if(root.data < val){
			root = root.right;
		}else {
			root = root.left;
		}

	}
	public static void preorder(Node root) {
		if(root != null) {
			System.out.print(root.data + " ");
			preorder(root.left);
			preorder(root.right);
		}
	}
	
	public static void inorder(Node root) {
		if(root != null) {
			inorder(root.left);
			System.out.print(root.data + " ");
			inorder(root.right);
		}
	}
	
	public static void postorder(Node root) {
		if(root != null) {
			postorder(root.left);
			postorder(root.right);
			System.out.print(root.data + " ");
		}
	}
	
	public static void main(String[] args) {
		Node root = null;
		root = addNodeBST(root, new Node(5, null));
		root = addNodeBST(root, new Node(4, null));
		root = addNodeBST(root, new Node(7, null));
		root = addNodeBST(root, new Node(1, null));
		root = addNodeBST(root, new Node(2, null));
		root = addNodeBST(root, new Node(3, null));
		root = addNodeBST(root, new Node(6, null));
		root = addNodeBST(root, new Node(8, null));
		root = addNodeBST(root, new Node(9, null));
		
		preorder(root);
		System.out.println();
		
		inorder(root);
		System.out.println();
		
		postorder(root);
		System.out.println();
		
		System.out.println(getMin(root).data);
		System.out.println(getMax(root).data);
	}

}
