import java.util.LinkedList;
import java.util.Queue;


public class PotD06072014_2 {

	static class NodeLevel{
		public Node node;
		public int level;
		
		public NodeLevel(Node node, int level) {
			this.node = node;
			this.level = level;
		}
	}
	
	public static void printTreeByLevel(Node root) {
		
		if(root == null) {
			return;
		}
		
		Queue<NodeLevel> q = new LinkedList<NodeLevel>();
		int currentLevel = 1;
		q.add(new NodeLevel(root, 1));
		
		while(q.isEmpty() == false) {
			NodeLevel temp = q.poll();
			int tempLevel = temp.level;
			
			if(temp.level > currentLevel) {
				currentLevel++;
				System.out.println();
			}
			
			System.out.print(temp.node.data + " ");
			
			if(temp.node.right != null) {
				q.add(new NodeLevel(temp.node.right, (tempLevel + 1)));
			}
			
			if(temp.node.left != null) {
				q.add(new NodeLevel(temp.node.left, (tempLevel + 1)));
			}
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
		
		printTreeByLevel(root);

	}

}
