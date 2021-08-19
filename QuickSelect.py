# QuickSelect: pick a pivot element, partition, then recurse on sublist containing index i

# Select an element p, apply partition(p)
# if i = index of p, done!
# if i< index of p, recurse left else right

# Median of Medians: Fast way to select a “good” pivot, guarantees pivot is greater than 30% of elements and less than 30% of the elements
# Worst case for Quick Select would be O(n) i.e. if the pivot is always the median, for that we use Median of Medians which uses QuickSelect as a subroutiine
# Median  of Medians breaks list into chunks of size 5,  finds the median of each chunk, return median of medians (using QuickSelect)
# Using QuickSelect to pick median guarantees Θ(n log n) run time


class QuickSelect:
    def select(self, A: [int], k: int) -> int:
        return self.kthSmallest(A, 0, len(A) - 1, k + 1)

    @staticmethod
    # basic swap function
    def swap(a, i, j):
        tmp = a[i]
        a[i] = a[j]
        a[j] = tmp

    def kthSmallest(self, A, left, right, k):
        if 0 < k <= right - left + 1:

            n = right - left + 1
            # storing median of each chunk
            median = []

            i = 0
            while i < n // 5:
                median.append(self.MedofMed(A, left + i * 5, 5))
                i += 1

            if i * 5 < n:
                median.append(self.MedofMed(A, left + i * 5,
                                            n % 5))
                i += 1

            # Median of Medians implementation
            if i == 1:
                MoM = median[i - 1]
            else:
                MoM = self.kthSmallest(median, 0,
                                       i - 1, i // 2)

            # obtain the index of pivot
            pivotpos = self.partition(A, left, MoM)

            if pivotpos - left == k - 1:
                return A[pivotpos]
            # recurse left
            if pivotpos - left > k - 1:
                return self.kthSmallest(A, left, pivotpos - 1, k)
            # recurse left
            return self.kthSmallest(A, pivotpos + 1, right, k - pivotpos + left - 1)
        return 0

    def MedofMed(self, a, m, n):
        lst = []
        for i in range(m, m + n):
            lst.append(a[i])

        # using built in sort function
        lst.sort()
        # get the middlemost element in the array
        return lst[n // 2]

    def partition(self, A: [int], low: int, high: int) -> int:
        # using partition code of QuickSort
        r = len(A) - 1
        q = high
        for i in range(low, r):
            if A[i] == q:
                self.swap(A, r, i)
                break
        q = A[r]
        i = low
        for j in range(i, r):
            if A[j] <= q:
                self.swap(A, i, j)
                i += 1
        self.swap(A, i, r)
        return i
