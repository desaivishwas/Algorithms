import random


class QuickSort:

    def partition(self, A, p, r):

        d = random.randint(p, r - 1)
        A[r - 1], A[d] = A[d], A[r - 1]
        x = A[r - 1]
        i = p
        for j in range(p, r - 1):
            if A[j] <= x:
                A[i], A[j] = A[j], A[i]
                i = i + 1
        A[i], A[r - 1] = A[r - 1], A[i]
        return i

    def sort(self, A, p, r):
        if p < r:
            pivot = self.partition(A, p, r)
            self.sort(A, p, pivot)
            self.sort(A, pivot + 1, r)
