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
            int n = in.nextInt();
            
            long res =  getMultiplesSum(3, n) + 
                        getMultiplesSum(5, n) -
                        getMultiplesSum(15, n);

            System.out.println(res);
        }
    }

    static long getMultiplesSum(int k, int n) { 
        long sections = (int) (n - 1) / k;
        long nextMax = (sections * k) + k;
        long total = nextMax * (int)(sections / 2);
        if(sections % 2 != 0) total += nextMax / 2;
        return total;
    }
}

