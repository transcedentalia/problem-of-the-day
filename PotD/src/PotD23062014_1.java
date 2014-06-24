import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.StringTokenizer;


public class PotD23062014_1 {

	public static void zeroizeLine(int[][] matrix, int n, int k) {
		for(int i = 0 ; i < n ; i++)
			matrix[k][i] = 0;
	}
	
	public static void zeroizeColumn(int[][] matrix, int m, int k) {
		for(int i = 0 ; i < m ; i++)
			matrix[i][k] = 0;
	}
	
	public static void zeroize(int[][] matrix, int n, int m) {
		if(matrix == null)
			return;
		
		int lines[] = new int[n];
		int columns[] = new int[m];
		
		for(int i = 0; i < n; ++i) {
			for(int j = 0; j < m; ++j)
				
				if(matrix[i][j] == 0) {
					lines[i] = 1;
					columns[j] = 1;
				}
		}
		
		for(int i = 0; i < n; ++i)
			if(lines[i] == 1)
				zeroizeLine(matrix, n, i);
		
		for(int j = 0; j < m; ++j)
			if(columns[j] == 1)
				zeroizeColumn(matrix, m, j);
		
			
	}
	
	public static void printMatrix(int[][] matrix, int n, int m) {
		for(int i = 0; i < n; ++i){
			for(int j = 0; j < m; ++j) {
				System.out.print(matrix[i][j] + " ");
			}
			System.out.println();
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new FileReader("Input"));
		StringTokenizer st  = new StringTokenizer(br.readLine());
		
		//Read n and m
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int matrix[][] = new int[n][m];
		
		for(int i = 0; i < n; ++i) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j < m; ++j) {
				matrix[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		zeroize(matrix, n, m);
		printMatrix(matrix, n, m);
		
		br.close();
	}
}
