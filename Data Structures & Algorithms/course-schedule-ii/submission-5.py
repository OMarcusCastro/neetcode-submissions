class Solution:

    def createAdj(self, prerequisites):
        adj = {}
        for a,b in prerequisites:
            adj[a] = adj.get(a,[])+[b]
        return adj

    def buildPath(self,curr,adj,visits,cycle):
        if cycle.get(curr)==1:
            return None
        if visits.get(curr)==1:
            return []

        visits[curr]=1
        cycle[curr]=1

        path =[]

        if adj.get(curr) is not None:
            for neighbor in adj[curr]:
                currPath=self.buildPath(neighbor,adj,visits,cycle)
                if currPath is None:
                    return None
                path += currPath
        
        path.append(curr)
        cycle[curr]=0

        return path

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=self.createAdj(prerequisites)
        visits = {}
        ans = []

        for i in range(numCourses):
            if visits.get(i)==1:
                continue
            currPath = (self.buildPath(i,adj,visits,{}))

            if currPath is None:
                return []
            ans+=currPath
        return ans