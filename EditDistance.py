class EditDistance:
    def editDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        # d[i][j] contains the edit distance of the two words at i & j i.e. word1[i:] and word2[j:]
        d = [[0] * (n+1) for _ in range(m+1)]
        for i in reversed(range(m+1)):
            for j in reversed(range(n+1)):
                if i == m:
                    d[i][j] = n -j
                elif j == n:
                    d[i][j] = m - i
                else:
                    c = 0 if word1[i] == word2[j] else 1
                    ins = d[i+1][j] + 1
                    de = d[i][j+1] + 1
                    sub = d[i+1][j+1] + c
                    d[i][j] = min(ins, de, sub)
        return d[0][0]



