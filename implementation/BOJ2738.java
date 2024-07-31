import java.util.Scanner;

public class BOJ2738 {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        int[][] data1= new int [n][m];
        int[][] data2= new int [n][m];
        for (int i=0; i<n;i++){
            for (int j=0; j<m;j++){
                data1[i][j]=sc.nextInt();
            }
        }
        for (int i=0; i<n;i++){
            for (int j=0; j<m;j++){
                data2[i][j]=sc.nextInt();
            }
        }
        for (int i=0; i<n;i++){
            for (int j=0; j<m; j++){
                System.out.print(data1[i][j]+data2[i][j]+" ");
            }
            System.out.println();
        }
    }
}
