import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();
        for(int a0 = 0; a0 < t; a0++){
            long n = in.nextLong();
            
            long prev1 = 1;
            long prev2 = 2;
            long res = 0;
            while(prev2 <= n){
                if(prev2 % 2 == 0) res += prev2;
                long temp = prev1 + prev2;
                prev1 = prev2;
                prev2 = temp;
            }
            System.out.println(res);
        }
    }
}

