
public class Solution {
    public static void main(String [] args){

        int n = 10;
        int r = 1;
        for(int i = 1; i < n ; i++){
           r = (r * (i + 1)) / gdc(r, i + 1);
        }
        System.out.println(r);
    }

    public static int gdc(int a, int b){
        if(a == 0) return b;
        return gdc(b % a, a);
    }
}
