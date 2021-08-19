# Algorithm referred from Python Interval Scheduling discussion on Leetcode

class Scheduling:

    @staticmethod
    def schedule(A: [[int]]) -> int:
        # sorting the jobs by their finishing time
        sortedA = sorted(A, key=lambda k: k[1])
        cnt = 0
        start_job = 90000
        end_j = -90000
        f = True

        for i in range(0, len(sortedA)):
            start, end = sortedA[i][0], sortedA[i][1]
            if start < end:
                if start >= end_j:
                    cnt += 1
                    end_j = end
                    start_job = start
            elif f:
                start_job = start
                end_j = end
                f = False

        # for jobs starting in midnight
        for i in range(0, len(sortedA)):
            start, end = sortedA[i][0], sortedA[i][1]
            if start > end:
                if start >= end_j:
                    cnt += 1
                    break
        # get the number of jobs
        return cnt

