import java.util.Arrays;

public class MergeSort {
    static void merge(int A[], int p, int q, int r)
    {
        int left[] = Arrays.copyOfRange(A, p, q+1);
        int right[] = Arrays.copyOfRange(A, q+1, r+1);

        int i = 0, j = 0, k = p;
        while (i < left.length && j < right.length) {
            if (left[i] <= right[j]) {
                A[k] = left[i];
                i++;
                k++;
            }
            else {
                A[k] = right[j];
                j++;
                k++;
            }
        }

        while (i < left.length) {
            A[k] = left[i];
            i++;
            k++;
        }

            while (j < right.length) {
                A[k] = right[j];
                j++;
                k++;
            }
    }

    static void sort(int A[], int p, int r)
    {

        int start = p, end =  r;
        if (start < end)
        {
            int q = (start + end ) / 2;
            sort(A, start, q);
            sort(A, q+1, end);
            merge(A, p, q, r);
        }
    }

    }
