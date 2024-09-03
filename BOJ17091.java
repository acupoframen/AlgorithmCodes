import java.util.Scanner;

public class BOJ17091 {
    private static final String[] hours = {
            "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"
    };
    private static final String[] minutes = {
            "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
            "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven",
            "twenty eight", "twenty nine", "half"
    };
    public static void main(String[] args) {

        Scanner sc= new Scanner(System.in);
        int h=sc.nextInt();
        int m=sc.nextInt();
        
        if (m == 0) {
        System.out.println(hours[h] + " o' clock");
    } else if (m <= 30) {
        if (m == 15 || m == 30) {
            System.out.println(minutes[m] + " past " + hours[h]);
        }
        else if (m==1){
            System.out.println(minutes[m] + " minute past " + hours[h]);
        }
        else {
            System.out.println(minutes[m] + " minutes past " + hours[h]);
        }
    } else {
        int minutesToNextHour = 60 - m;
        int nextHour = (h % 12) + 1;
        if (minutesToNextHour == 15) {
            System.out.println("quarter to " + hours[nextHour]);
        }
        else if(minutesToNextHour==1){
            System.out.println("one minute to "+ hours[nextHour]);
            }
        else {
            System.out.println(minutes[minutesToNextHour] + " minutes to " + hours[nextHour]);

        }
    }

        sc.close();
    }
}
