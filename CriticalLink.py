from collections import defaultdict


class CriticalLink:
    def __init__(self):
        self.cur = 0

    def criticalLink(self, n: int, links: [[int]]) -> int:
        graph = defaultdict(list)
        for v in links:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])

        d = [None for i in range(n)]
        low = [None for i in range(n)]
        cur = 0
        start = 0
        res = []

        def dfs(node, parent):
            if d[node] is None:
                d[node] = self.cur
                low[node] = self.cur
                self.cur += 1
                for n in graph[node]:
                    if d[n] is None:
                        dfs(n, node)

                if parent is not None:
                    l = min([low[i] for i in graph[node] if i != parent] + [low[node]])
                else:
                    l = min(low[i] for i in graph[node] + [low[node]])
                low[node] = l

        dfs(0, None)

        for v in links:
            if low[v[0]] > d[v[1]] or low[v[1]] > d[v[0]]:
                res.append(v)
        result = len(res)
        return result

# if __name__ == "__main__":
#   links = [[0, 1], [1, 2], [2, 0], [1, 3]]
#  c = CriticalLink().criticalLink(4, links)
# print(c)
