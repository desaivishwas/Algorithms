class StronglyConnectedComponents:
    def scc(self, students: int, knows: [[int]]) -> [[int]]:
        self.graph = {x: [] for x in range(students)}
        for n1, n2 in knows:
            self.addEdge(n1, n2, True)
        stack = []
        visited = [False] * students
        for i in range(students):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        self.tmp = []
        self.getTranspose(students)
        visited = [False] * students
        result = []
        while stack:
            i = stack.pop()
            if visited[i] == False:
                self.DFSUtil(i, visited)
                result.append(self.tmp)
                self.tmp = []
        return result

    def addEdge(self, n1, n2, flag):
        if flag:
            self.graph[n1].append(n2)
        else:
            self.transpose[n1].append(n2)

    def DFSUtil(self, node, visited):
        visited[node] = True
        self.tmp.append(node)
        for elem in self.transpose[node]:
            if visited[elem] == False:
                self.DFSUtil(elem, visited)

    def fillOrder(self, node, visited, stack):
        visited[node] = True
        for elem in self.graph[node]:
            if visited[elem] == False:
                self.fillOrder(elem, visited, stack)
        stack = stack.append(node)

    def getTranspose(self, students):
        self.transpose = {x: [] for x in range(students)}
        for i in self.graph:
            for j in self.graph[i]:
                self.addEdge(j, i, False)