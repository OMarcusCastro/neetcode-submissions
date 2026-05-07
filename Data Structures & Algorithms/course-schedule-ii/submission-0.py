class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        visited = set()
        in_cycle = set()

        for a, b in prerequisites:
            if adj.get(b) is None:
                adj[b] = []
            adj[b].append(a)

        def dfs(course, adj):
            if course in in_cycle:
                return None
            if course in visited:
                return []

            in_cycle.add(course)

            ans = []
            for neighbor in adj.get(course, []):
                sub = dfs(neighbor, adj)
                if sub is None:
                    return None
                ans += sub

            in_cycle.remove(course)
            visited.add(course)
            ans.append(course)
            return ans

        result = []
        for course in range(numCourses):
            sub = dfs(course, adj)
            if sub is None:
                return []
            result += sub

        return result[::-1]  # <-- aqui