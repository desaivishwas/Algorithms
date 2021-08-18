public class Fibonacci {
    static int fibonacci(int n) {
        //assert (n > 0) && (n <= 46) : "n out of range";
        if((n==0)||n==1)
            return n;
        int a,b,c;
        b=c=1;
        for(int i=3;i<=n;i++) {
                a=b;
                b=c;
                c=a+b;
        }
        return c;
    }

}