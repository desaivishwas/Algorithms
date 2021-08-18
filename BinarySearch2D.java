public class BinarySearch2D {
    static int[] search(int[][] M, int q) {
        if(M==null || M.length==0 || M[0].length==0)
            return new int[]{-1 , -1};

        int i = M.length, j = M[0].length, begin = 0, end = i*j-1;
        while(begin <= end){
            int mid= (begin + end) / 2;
            //coordinates
            int x = mid / j, y = mid % j;

            if(M[x][y] == q)
                return new int[] {x, y}; ;

            if(M[x][y] < q)
                begin = mid + 1;

            else
                end = mid - 1;
        }
        return new int[]{-1 , -1} ;
    }

}

