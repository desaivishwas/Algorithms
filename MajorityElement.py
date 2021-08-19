class MajorityElement:
    def majority(self, A):
        c = self.find_ele(A)

        # Print element if it is the majority
        if self.is_Majority(A, c):
            return c
        else:
            return -1

    # function to choose the element
    @staticmethod
    def find_ele(A):
        maj_index = 0
        count = 1
        for i in range(len(A)):
            if A[maj_index] == A[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_index = i
                count = 1
        return A[maj_index]

    # function to check if the element is the majority or not
    @staticmethod
    def is_Majority(A, cand):
        count = 0
        for i in range(len(A)):
            if A[i] == cand:
                count += 1
        if count > len(A) / 2:
            return True
        else:
            return False
