import java.util.Scanner;

public class BOJ14909 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer = 0;
        while (sc.hasNextInt()) {
            int num = sc.nextInt();
            if (num > 0)
                answer++;

        }
        System.out.println(answer);
        sc.close();
    }
}
