import static org.junit.Assert.*;

public class InsertionSort {
    static void sort(int A[]) {
        int n = A.length;
        for (int j = 0; j < n; j++) {
            //assert(0<=j && j<=n);
            assertTrue(sorted(A, 0 , j));
            int key = A[j];
            int i = j - 1;
            while ((i > -1) && (A[i] > key)) {
                //assert(0<=i+1 && i+1<=j);
                assertTrue(sorted(A, 0 , i+1));
                assertTrue(sorted(A, i+1 , j+1));
                A[i + 1] = A[i];
                i--;
            }
            A[i + 1] = key;
        }
    }

    static Boolean sorted(int A[], int begin, int end) {
        for (int i = begin; i != end; ++i) {
            if (i + 1 != end) {
                if (A[i] > A[i + 1]) return false;
            }
        }
        return true;
    }
}