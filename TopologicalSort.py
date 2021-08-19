from collections import defaultdict

class TopologicalSort:
    def topoSort(self, pre_requisites: [[int]], total_courses: int) -> [int]:
        pre = {c: [] for c in range(total_courses)}
        for course, pre_req in pre_requisites:
            pre[course].append(pre_req)

        output = []
        visit, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True

            cycle.add(course)
            for p in pre[course]:
                if not dfs(p):
                    return False
            cycle.remove(course)
            output.append(course)
            visit.add(course)
            return True

        for course in range(total_courses):
            if not dfs(course):
                return []

        return output[::-1] if len(output) == total_courses else []
