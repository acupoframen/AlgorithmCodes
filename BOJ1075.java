import java.util.Scanner;

public class BOJ1075 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int f=sc.nextInt();
        n-=n%100;
        while (true){
            if (n%f==0){
                break;
            }
            n++;
        }
    System.out.format("%02d",(n%100));
    }
}
