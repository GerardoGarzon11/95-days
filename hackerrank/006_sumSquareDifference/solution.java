import java.math.BigInteger;

public class Solution {
    public static void main (String [] args){
        int n = 100;

//        long sumOfNums = (n * (n + 1)) / 2;
//        long sumOfSquares = (n * (n + 1) * ((2 * n) + 1)) / 6;
//
//        long a = ((long)Math.pow(sumOfNums, 2)) - sumOfSquares;

        BigInteger sumOfNums = new BigInteger("1")
                .multiply(new BigInteger(Integer.toString(n))).add(new BigInteger("1"))
                .multiply(new BigInteger(Integer.toString(n)))
                .divide(new BigInteger("2"));

        BigInteger sumOfSquares = new BigInteger("1")
                .multiply(new BigInteger("2")).multiply(new BigInteger(Integer.toString(n)))
                    .add(new BigInteger("1"));

        BigInteger sumOfSquares2 = new BigInteger("1")
                .multiply(new BigInteger(Integer.toString(n))).add(new BigInteger("1"))
                .multiply(new BigInteger(Integer.toString(n)));

        sumOfSquares = sumOfSquares.multiply(sumOfSquares2).divide(new BigInteger("6"));


        System.out.println(sumOfNums.pow(2).subtract(sumOfSquares));
    }
}
