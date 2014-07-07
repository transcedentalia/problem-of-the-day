
public class PotD02072014_2 {

	static class MyNode {
		public String data;
		public MyNode left;
		public MyNode right;
		
		public MyNode(String data, MyNode left, MyNode right) {
			this.data = data;
			this.left = left;
			this.right = right;
		}
	}
	
	public static int getExpressionResult(MyNode root) {
		
		if(root == null) {
			return 0;
		}

		if(root.data == "+"){
			return getExpressionResult(root.left) + getExpressionResult(root.left);
		}
		if(root.data == "-"){
			return getExpressionResult(root.left) - getExpressionResult(root.left);
		}
		if(root.data == "*"){
			return getExpressionResult(root.left) * getExpressionResult(root.left);
		}
		if(root.data == "/"){
			return getExpressionResult(root.left) / getExpressionResult(root.left);
		}
		
		return Integer.parseInt(root.data);
	}
	
	public static void main(String[] args) {
		MyNode root = new MyNode("+", 
								 new MyNode("+", 
										  new MyNode("2", null, null), 
										  new MyNode("3", null, null)), 
								new MyNode("+", 
										 new MyNode ("1", null, null), 
										 new MyNode("1", null, null)));
			
		System.out.println(getExpressionResult(root));

	}

}
