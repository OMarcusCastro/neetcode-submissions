class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for course,prerequisite in prerequisites:
            if adj.get(prerequisite) is None:
                adj[prerequisite]=[]
            adj[prerequisite].append(course)
        # print(adj)

        def dfs(numCourse,adj,path,visits):
            # print("visits",visits,numCourse)
            if numCourse in path:
                # print("passei")
                return False
            if numCourse in visits:
                return True
            
            path.add(numCourse)
            if adj.get(numCourse)is not None:
                for neighbor in adj[numCourse]:
                    # print("neighbor",neighbor,"visits",visits)
                    if dfs(neighbor,adj,path,visits)==False:
                        return False
            path.remove(numCourse)
            visits.add(numCourse)
            return True

        visits = set()
        # path = set()
        for course in range(numCourses):
            path = set()
            r=dfs(course,adj,path,visits)
            if r == False:
                return False
        return True