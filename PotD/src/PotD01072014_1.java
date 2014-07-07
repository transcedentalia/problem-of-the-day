
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
			newNode.parent = root;
			root.right = addNodeBST(root.right, newNode);
		}
		
		if(root.data > newNode.data) {
			newNode.parent = root;
			root.left = addNodeBST(root.left, newNode);
		}
			
		return root;
	}
	
	public static Node deleteNodeBST(Node root, int val, int direction)
	{
		
		if(root == null) {
			return null;
		}
		
		if(root.data == val) {
			
			if(root.left == null && root.right == null ) {
				if(root.parent != null) {
					if(direction == 0) {
						root.parent.left = null;
					}
					else {
						root.parent.right = null;
					}
				}else {
					//this is the root
					root = null;
				}
			}else if(root.right != null) {
						
				Node temp = root.right;
				if(temp.left == null) {
					root.data = temp.data;
					root.right = temp.right;
				}else {
					while(temp.left != null) {
						temp = temp.left;
					}
					
					root.data = temp.data;
					temp.parent.left = null;
				}
				
			}else if(root.left != null) {
				
				Node temp = root.left;
				if(temp.right == null) {
					root.data = temp.data;
					root.left = temp.left;
				}else {
					while(temp.right != null) {
						temp = temp.right;
					}
					
					root.data = temp.data;
					temp.parent.right = null;
				}
				
			}
		}
		
		if(root.data < val){
			deleteNodeBST(root.right, val, 1);
		}else {
			deleteNodeBST(root.left, val, 0);
		}
		
		return root;

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
		
		deleteNodeBST(root, 9, 0);
		inorder(root);
		System.out.println();
	}
}
