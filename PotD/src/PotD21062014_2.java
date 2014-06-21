
public class PotD21062014_2 {

	public static void rotate90CW(char[][] matrix, int n) {
		
		char[][] matrix90CW = new char[n][n];
		
		for(int i = 0; i < n; ++i) 
			for(int j = 0; j < n; ++j)
				matrix90CW[j][n - i - 1] = matrix[i][j];
		
		printMatrix(matrix90CW, 3);

	}
	
	public static void printMatrix(char[][] m, int n) {
		
		if(m == null)
			return;
		
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < n ; ++j) {
				System.out.print(m[i][j] + " ");
			}
			System.out.println();
		}
		
		System.out.println();
	}
		
	public static void main(String[] args) {
		char[][] matrix = new char[4][4];
		matrix[0][0] = '1';
		matrix[0][1] = '2';
		matrix[0][2] = '3';
		matrix[1][0] = '4';
		matrix[1][1] = '5';
		matrix[1][2] = '6';
		matrix[2][0] = '7';
		matrix[2][1] = '8';
		matrix[2][2] = '9';
		
		rotate90CW(matrix, 3);
		
	}

}
