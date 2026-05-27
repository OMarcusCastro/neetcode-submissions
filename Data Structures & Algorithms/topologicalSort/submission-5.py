def buildAdj(edges):
    adj = {}
    for u,v in edges:
        adj[u] = adj.get(u,[])+[v]
    return adj

def dfs(curr,adj,visits,currPath,topSort):

    if currPath.get(curr,0)==1:
        return False

    if visits[curr]==1:
        return True
    
    visits[curr]=1
    currPath[curr] = 1

    for nei in adj.get(curr,[]):
        if dfs(nei,adj,visits,currPath,topSort) is False:
            return False
    topSort.append(curr)

    currPath[curr]=0
    


def topologicalSortRun(n: int, edges: List[List[int]]):
    adj = buildAdj(edges)
    visits = [0]*n
    path = []
    for i in range(n):
        if visits[i]==1:
            continue
        if dfs(i,adj,visits,{},path) is False:
            return []
    return path[::-1]
        

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        return topologicalSortRun(n,edges)