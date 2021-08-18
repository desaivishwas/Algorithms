//import java.util.Arrays;
public class BinarySearch {
    static int search(int A[], int key) {
        return binarySearch(A, 0, A.length - 1, key);
    }

    private static int binarySearch(int arr[] , int left, int right, int key) {
        int n = arr.length, mid;
        //int[] newArray = Arrays.copyOfRange(A, startIndex, endIndex);

        if (left > right) {
            return -1;
            }
        else
            mid = (left + right)/ 2;
            if (key == arr[mid])
                return mid;
            else if (key < arr[mid]){
                   // left = mid + 1
                    return binarySearch(arr, left, mid-1,key);}
                else{
                     //right = mid  - 1;
                     return binarySearch(arr, mid+1, right,key);}
        }

    }


