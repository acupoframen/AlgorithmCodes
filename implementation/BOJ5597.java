package implementation;

import java.util.Scanner;

public class BOJ5597 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int[] student = new int[31];
        for (int i=0; i<28; i++){
            int num=sc.nextInt();
            student[num]=1;
        }
        for (int i=1;i<student.length;i++){
            if (student[i]==0)
            System.out.println(i);
        }
        sc.close();
    }
}
