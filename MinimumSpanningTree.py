from collections import defaultdict

class MinimumSpanningTree:

    def mst(self, edges: [[int]], vertices: int) -> int:
        self.graph = []
        self.add_edges(edges)
        return self.KruskalsMST(vertices)

    def add_edges(self, edges):
        for u, v, w in edges:
            self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalsMST(self, vertices):
        # result = []
        cost = 0
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(vertices):
            parent.append(node)
            rank.append(0)

        while e < vertices - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                cost += w
                self.union(parent, rank, x, y)
        return cost