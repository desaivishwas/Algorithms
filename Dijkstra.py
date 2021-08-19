import sys

class Dijkstra:
    def shortestDistance(self, edges, vertices):
        self.graph = {x: [] for x in range(vertices)}
        self.fill_graph(edges, vertices)
        print(self.graph)
        if vertices == 1:
            return [0]
        if vertices == 0:
            return []
        minDist = self.djikstras(vertices)
        for index in range(len(minDist)):
            if minDist[index] == sys.maxsize:
                minDist[index] = -1
        return minDist

    def fill_graph(self, edges, vertices):
        for n1, n2, distance in edges:
            self.graph[n1] += [(n2, distance)]

    def min_distance(self, minDist, s_vertices, vertices):
        min_val = sys.maxsize
        min_node = -1
        for node in range(vertices):
            if minDist[node] < min_val and not s_vertices[node]:
                min_val = minDist[node]
                min_node = node
        return min_node

    def successors(self, node):
        return self.graph[node]

    def djikstras(self, vertices):
        start_node = 0
        minDist = [sys.maxsize] * vertices
        minDist[start_node] = 0
        s_vertices = [False] * vertices

        for node in range(vertices):
            min_index = self.min_distance(minDist, s_vertices, vertices)
            if min_index == -1:
                continue
            s_vertices[min_index] = True
            for v, dist in self.successors(min_index):
                if dist > 0 and not s_vertices[v] and minDist[v] > minDist[min_index] + dist:
                    minDist[v] = minDist[min_index] + dist

        return minDist