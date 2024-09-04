package Math;

import java.util.Scanner;

public class BOJ9610 {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        int q1 = 0, q2=0, q3=0, q4 = 0, a = 0;
        for (int i=0;i<n;i++){
            int x=sc.nextInt();
            int y=sc.nextInt();
            if (x==0||y==0){
                a+=1;
            }
            else if (x>0){
                if (y>0)
                    q1+=1;
                else
                    q4+=1;
            }
            else{
                if (y>0)
                    q2+=1;
                else
                    q3+=1;
            }
        }
        System.out.println("Q1: "+q1);
        System.out.println("Q2: "+q2);
        System.out.println("Q3: "+q3);
        System.out.println("Q4: "+q4);
        System.out.println("AXIS: "+a);
        sc.close();
    }
}
