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

            long lastFactor;
            long factor = 2;
            if(n % 2 == 0) {
                lastFactor = 2;
                while (n % 2 == 0) n = n/2;
            } else {
                lastFactor = 1;
            }

            factor = 3;
            double maxFactor = Math.sqrt(n);
            while (n > 1 && factor <= maxFactor){
                if(n % factor == 0){
                    n = n / factor;
                    lastFactor = factor;
                    while (n % factor == 0) n = n / factor;
                    maxFactor = Math.sqrt(n);
                }
                factor += 2;
            }

            if(n == 1){
                System.out.println(lastFactor);
            } else {
                System.out.println(n);
            }

        }
    }
}

