class HeapSort:

    def heapify(self, A, n, i):
        # Initialize largest as root
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        # check if left is greater than root
        if left < n and A[left] > A[i]:
            largest = left
        # check if right is greater than root
        if right < n and A[right] > A[largest]:
            largest = right
        if largest != i:
            # swap
            A[i], A[largest] = A[largest], A[i]
            # Heapify the root
            self.heapify(A, n, largest)

    # HeapSort(A)
    def heapSort(self, A):
        n = len(A)

        # Build-Max-Heap(A)
        for i in range(n//2 -1, -1, -1):
            self.heapify(A, n, i)


        for i in range(n-1, 0, -1):
            A[i], A[0] = A[0], A[i]
            #n = n - 1
            self.heapify(A, i, 0)
