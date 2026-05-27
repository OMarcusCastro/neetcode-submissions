def buildAdj(edges):
    adj = {}
    for u,v in edges:
        adj[u] = adj.get(u,[])+[v]
    return adj

def dfs(curr,adj,visits,currPath):

    if currPath.get(curr,0)==1:
        return None

    if visits[curr]==1:
        return []

    currPath[curr]=1



    path = []

    for nei in adj.get(curr,[]):
        neiPath = dfs(nei,adj,visits,currPath)
        if neiPath is None:
            return None
        path+=neiPath

    path.append(curr)
    visits[curr]=1
    currPath[curr]=0
    return path


def topologicalSortRun(n: int, edges: List[List[int]]):
    adj = buildAdj(edges)

    visits = [0]*n
    path = []
    for i in range(n):
        if visits[i] == 0:
            x= dfs(i,adj,visits,{})
            if x is None:
                path = []
                break
            path+=x
    return path[::-1]
        




class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        return topologicalSortRun(n,edges)
        