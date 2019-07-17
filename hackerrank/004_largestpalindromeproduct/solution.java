public class Solution {
    public static void main (String [] args) {
        int n = 800000;
        int a = 0;
        for(int i = 100; i <= 999; i++){
            for(int j = 100; j <= 999; j++){
                int prod = i * j;
                if(prod < n){
                    int reverse = 0;
                    int num = prod;
                    while(num != 0){
                        reverse = (reverse * 10) + num % 10;
                        num = num/10;
                    }
                    if(reverse == prod && prod > a){
                        a = reverse;
                    }
                }
            }
        }
        System.out.println(a);
    }
}
