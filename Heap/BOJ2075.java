import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.StringTokenizer;

public class BOJ2075 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n= Integer.parseInt(br.readLine());
        PriorityQueue <Integer> queue= new PriorityQueue<>();
        StringTokenizer st= null;
        for (int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            for (int j=0;j<n;j++){
                int num=Integer.parseInt(st.nextToken());
                if (queue.size()==n){
                    if (queue.peek()<num){
                        queue.poll();
                        queue.add(num);
                    }
                }

                else queue.add(num);
            }
        }
        System.out.println(queue.poll());
    }
}
