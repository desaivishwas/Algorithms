## test file: FamilyForestTest.py
from collections import defaultdict


class FamilyForest:
    # CLRS 21.3
    fam = {}

    def make_family(self, s: str) -> None:
        family = self.fam
        family[s] = 1

    def union(self, s: str, t: str) -> str:
        f = self.fam
        p = ""
        if type(f[s]) and type(f[t]) == int:
            x = f[s]
            y = f[t]
            f[t] = s
            f[s] = x + y
            p = s
        else:
            p1 = self.find(s)
            p2 = self.find(t)
            w1 = f[p1]
            w2 = f[p2]

            if w1 > w2:
                p = p1
                f[p2] = p1
                f[p1] = w1 + w2
            else:
                p = p2
                f[p1] = p2
                f[p2] = w1 + w2

        return p

    def find(self, s: str) -> str:
        f = self.fam
        if isinstance(f[s], int):
            return s
        else:
            return self.find(f[s])
