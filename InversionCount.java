





public static class MaxSurpasser {
    int[] A, rank, surp, mergedRank;

    private MaxSurpasser(int[] a) {
        this.A = a;
        this.rank = new int[a.length];
        this.surp = new int[a.length];
        this.mergedRank = new int[a.length];
        for (int i = 0; i < rank.length; i++){
            rank[i] = i;
        }
    }

    public static int find(int[] a) {
        return new MaxSurpasser(a).sort();
    }

    private int sort() {
        mergeSort(0, A.length - 1);
        int max = 0;

        for (int i = 0; i < A.length; i++) {
            System.out.print(surp[i]+", ");
            if (surp[i] > max) {
                max = surp[i];
            }
        }
        return max;
    }

    private void mergeSort(int l, int r) {
        if (l >= r) {
            return;
        }
        //divide
        int q = (l + r) / 2;
        mergeSort(l, q);
        mergeSort(q + 1, r);
        //conquer
        int i = l;
        int j = q + 1; int acc = 0;
        //accumulate through merge
        for (int s = l; s <= r; s++) {
            if (j <= r && (i > q || A[rank[i]] < A[rank[j]])){
                mergedRank[s] = rank[j];
                acc++;
                j++;
            }
            else{
                mergedRank[s] = rank[i];
                surp[rank[i]] += acc;
                i++;
            }
        }
        for (int s = l; s <= r; s++) {
            rank[s] = mergedRank[s];
        }
    }
}







